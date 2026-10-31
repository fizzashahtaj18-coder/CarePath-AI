"""One small wrapper around the LLM API, so the provider can be swapped (ADR-6).

Claude Haiku 5.5 notes (from Anthropic's migration guide):
  - do NOT send temperature/top_p/top_k (they return an error)
  - a forced tool_choice is supported and gives reliable structured output
  - string values in tool calls may end with a newline, so we strip them
"""
import json

TOOL_NAME = "submit_checklist"


class LLMError(Exception):
    pass


class AnthropicClient:
    def __init__(self, api_key, model="claude-haiku-5-5", max_tokens=4000):
        import anthropic  # imported here so tests run without the package
        self._client = anthropic.Anthropic(api_key=api_key)
        self.model = model
        self.max_tokens = max_tokens

    def call_tool(self, system, user, tool_schema, tool_description):
        resp = self._client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=system,
            tools=[{"name": TOOL_NAME, "description": tool_description, "input_schema": tool_schema}],
            tool_choice={"type": "tool", "name": TOOL_NAME},
            messages=[{"role": "user", "content": user}],
        )
        for block in resp.content:
            if getattr(block, "type", None) == "tool_use":
                usage = {"input_tokens": resp.usage.input_tokens, "output_tokens": resp.usage.output_tokens}
                return strip_strings(block.input), usage
        raise LLMError("The model did not return a checklist.")


class FakeClient:
    """Test double: returns a prepared answer instead of calling an API."""

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = 0

    def call_tool(self, system, user, tool_schema, tool_description):
        self.calls += 1
        if not self.responses:
            raise LLMError("No more fake responses")
        return self.responses.pop(0), {"input_tokens": 0, "output_tokens": 0}


def strip_strings(value):
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        return [strip_strings(v) for v in value]
    if isinstance(value, dict):
        return {k: strip_strings(v) for k, v in value.items()}
    return value


def schema_for_tool(model_cls):
    """Pydantic JSON schema, with $defs inlined so every provider accepts it."""
    schema = model_cls.model_json_schema()
    defs = schema.pop("$defs", {})

    def resolve(node):
        if isinstance(node, dict):
            if "$ref" in node:
                return resolve(defs[node["$ref"].split("/")[-1]])
            return {k: resolve(v) for k, v in node.items()}
        if isinstance(node, list):
            return [resolve(v) for v in node]
        return node

    return json.loads(json.dumps(resolve(schema)))
