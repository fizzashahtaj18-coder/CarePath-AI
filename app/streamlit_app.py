"""CarePath AI: Sprint 1 app.

Stories: CPA-20 (appointment details), CPA-17 (paste text and call notes), CPA-21 (draft checklist).
Plus an Evaluation page (PM only) that scores the real model against the 10 synthetic test sets.

Run locally:  streamlit run app/streamlit_app.py
Secrets (.streamlit/secrets.toml locally, or App settings > Secrets on Streamlit Cloud):
  LLM_API_KEY    = "..."                 required
  LLM_MODEL      = "claude-haiku-5-5"    optional
  ACCESS_CODE    = "..."                 optional: visitors must enter it to use the app
  EVAL_PASSWORD  = "..."                 required to open the Evaluation page
"""
import datetime as dt
import io
import json
import os
import sys
import zipfile

import streamlit as st

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
for p in (HERE, os.path.join(ROOT, "eval")):
    if p not in sys.path:
        sys.path.insert(0, p)

from pipeline.checklist import PROMPT_VERSION, generate_checklist  # noqa: E402
from pipeline.ingest import read_file  # noqa: E402
from pipeline.llm import AnthropicClient, LLMError  # noqa: E402

PRICE_IN, PRICE_OUT = 0.10, 0.50  # USD per million tokens, Claude Haiku 5.5 (prompts under 100K tokens), checked Oct 2026
SPECIALTIES = ["Cardiology", "Dermatology", "Endocrinology", "ENT", "Gastroenterology",
               "Neurology", "Orthopedics", "Pulmonology", "Rheumatology", "Other"]
NOTICE = "CarePath AI helps you organize appointment instructions. It does not give medical advice."

st.set_page_config(page_title="CarePath AI", layout="centered")


def secret(name, default=None):
    try:
        return st.secrets.get(name, default)
    except Exception:  # no secrets file at all
        return default


def get_client():
    key = secret("LLM_API_KEY")
    if not key:
        st.error("The app isn't configured yet: add LLM_API_KEY in the app's secrets.")
        st.stop()
    return AnthropicClient(api_key=key, model=secret("LLM_MODEL", "claude-haiku-5-5"))


def api_error_message(e):
    """The provider's own error text (never includes the API key)."""
    body = getattr(e, "body", None)
    if isinstance(body, dict):
        err = body.get("error", body)
        if isinstance(err, dict) and err.get("message"):
            return err["message"]
    return str(e)[:500]


def cost(usage):
    return usage["input_tokens"] / 1e6 * PRICE_IN + usage["output_tokens"] / 1e6 * PRICE_OUT


# ---------------------------------------------------------------- access gate
code = secret("ACCESS_CODE")
if code and not st.session_state.get("access_ok"):
    st.title("CarePath AI")
    st.caption(NOTICE)
    entered = st.text_input("Access code", type="password")
    if entered:
        if entered == code:
            st.session_state.access_ok = True
            st.rerun()
        st.error("That code isn't right.")
    st.stop()

page = st.sidebar.radio("Page", ["Prepare for my appointment", "Evaluation (PM)"])
st.sidebar.caption("Prototype · synthetic data only · not HIPAA compliant · not clinically validated")


# ---------------------------------------------------------------- patient page
def prepare_page():
    ss = st.session_state
    ss.setdefault("docs", [])
    ss.setdefault("result", None)

    st.title("Get ready for your first specialist visit")
    st.info(NOTICE)

    st.subheader("1 · Your appointment")
    c1, c2 = st.columns(2)
    specialty = c1.selectbox("Specialty", SPECIALTIES)
    date = c2.date_input("Appointment date", value=None, format="MM/DD/YYYY")
    clinic = st.text_input("Clinic name (optional)")

    st.subheader("2 · Your documents")
    st.caption("Paste appointment instructions, or type what the clinic told you on the phone.")
    st.warning("Only add appointment instructions and referral letters. You don't need test results or medical records. "
               "Your text is sent to an AI service to create your checklist and isn't saved after you close this page. "
               "**This prototype is for synthetic (made-up) examples only.**")
    with st.form("add_text", clear_on_submit=True):
        label = st.text_input("Label", placeholder="For example: Phone call notes, Oct 28")
        text = st.text_area("Paste or type text", height=150,
                            placeholder="Paste instructions, or type what the clinic told you on the phone")
        if st.form_submit_button("Add text") and text.strip():
            doc_id = f"D{len(ss.docs) + 1}"
            ss.docs.append({"id": doc_id, "title": label.strip() or f"Document {doc_id}", "text": text})
            ss.result = None

    if ss.docs:
        st.markdown(f"**Added ({len(ss.docs)})**")
        for i, d in enumerate(list(ss.docs)):
            a, b = st.columns([5, 1])
            a.markdown(f"`{d['id']}` **{d['title']}** · {len(d['text'].split())} words")
            if b.button("Remove", key=f"rm{i}"):
                ss.docs.pop(i)
                for n, doc in enumerate(ss.docs, start=1):
                    doc["id"] = f"D{n}"
                ss.result = None
                st.rerun()

    st.subheader("3 · Your checklist")
    if st.button("Create my checklist", type="primary", disabled=not ss.docs):
        appointment = {"specialty": specialty, "date": str(date) if date else "", "clinic": clinic}
        with st.spinner("Reading your documents… (about 10–30 seconds)"):
            try:
                ss.result = generate_checklist(get_client(), ss.docs, appointment)
            except (LLMError, ValueError) as e:
                st.error(f"Something went wrong creating your checklist. Your documents are still here. Try again. ({e})")
            except Exception as e:  # network or API errors
                st.error("The AI service couldn't create your checklist. Your documents are still here. Try again.")
                with st.expander("Technical details (for the product team)"):
                    st.code(f"{type(e).__name__}: {api_error_message(e)}")
    if not ss.docs:
        st.caption("Add at least one document first.")

    r = ss.result
    if r:
        show_checklist(r)

    st.divider()
    if st.button("Delete everything"):
        for k in ("docs", "result"):
            ss.pop(k, None)
        st.success("All your documents and checklist data have been deleted.")
        st.rerun()


def show_checklist(r):
    if r["outcome"] == "no_instructions_found":
        st.warning("We didn't find appointment instructions in these documents.")
        return
    st.caption("**Draft:** nothing is final until you review it. Each item shows where it came from. "
               "(Checking sources and editing arrive in the next sprints.)")
    for c in r["conflicts"]:
        with st.container(border=True):
            st.markdown(f"🚩 **Conflicting instructions: {c['topic']}**")
            for x in c["citations"]:
                st.markdown(f"- “{x['quote']}” · `{x['chunk_id']}`")
            st.markdown("**Ask the clinic which is correct.** CarePath AI doesn't choose for you.")
    for cat, title in [("Bring", "Bring"), ("Do", "Do"), ("Before-date", "Before your visit")]:
        items = [i for i in r["items"] if i["category"] == cat]
        if not items:
            continue
        st.markdown(f"#### {title}")
        for i in items:
            with st.container(border=True):
                due = f" · by {i['due_date']}" if i.get("due_date") else ""
                st.markdown(f"**{i['text']}**{due}")
                if i["medical_instruction"]:
                    st.markdown("⚠️ *Medical instruction, shown in the original wording. "
                                "Confirm with your care team if you have questions.*")
                st.caption(" · ".join(f"`{c['chunk_id']}`" for c in i["citations"]))
    st.caption(f"Model: {secret('LLM_MODEL', 'claude-haiku-5-5')} · prompt {PROMPT_VERSION} · "
               f"attempts: {r['attempts']} · estimated cost ${cost(r['usage']):.4f}")


# ---------------------------------------------------------------- evaluation page
def evaluation_page():
    st.title("Evaluation (PM only)")
    pw = secret("EVAL_PASSWORD")
    if not pw:
        st.error("Set EVAL_PASSWORD in the app's secrets to use this page.")
        st.stop()
    if st.text_input("Evaluation password", type="password") != pw:
        st.stop()

    import run_eval  # eval/run_eval.py

    st.markdown("Runs the **real model** on all 10 synthetic test sets and scores it against the answer keys. "
                "Cost is about **$0.02** per run.")
    run_name = st.text_input("Run name", value=f"{secret('LLM_MODEL', 'claude-haiku-5-5')}_{PROMPT_VERSION}_{dt.date.today()}")
    if not st.button("Run evaluation", type="primary"):
        return

    client = get_client()
    testset = os.path.join(ROOT, "eval", "testset")
    set_ids = sorted(d for d in os.listdir(testset) if d.startswith("set"))
    outputs, total = {}, {"input_tokens": 0, "output_tokens": 0}
    bar = st.progress(0.0)
    for n, set_id in enumerate(set_ids, start=1):
        key = json.load(open(os.path.join(testset, set_id, "answer_key.json"), encoding="utf-8"))
        docs = []
        for d in key["documents"]:
            text, err = read_file(os.path.join(testset, set_id, d["file"]))
            docs.append({"id": d["id"], "title": d["title"], "text": text, "error": err})
        try:
            out = generate_checklist(client, docs, {"specialty": key["specialty"]})
        except Exception as e:
            st.warning(f"{set_id}: failed ({e}). Scored as an empty output.")
            out = {"outcome": "checklist", "items": [], "conflicts": [], "missing_topics": [], "document_errors": [],
                   "usage": {"input_tokens": 0, "output_tokens": 0}}
        outputs[set_id] = out
        for k in total:
            total[k] += out.get("usage", {}).get(k, 0)
        bar.progress(n / len(set_ids), text=f"{set_id} done")

    summary, rows, md = run_eval.evaluate(outputs, run_name)
    st.subheader("✅ PASS" if summary["overall_pass"] else "❌ FAIL")
    cols = st.columns(4)
    for col, (name, m) in zip(cols, [(k, v) for k, v in summary.items() if k != "overall_pass"]):
        shown = f"{m['value']:.0%}" if name != "Medical advice flags" else str(m["value"])
        col.metric(name, shown, help=f"Target: {m['target']}")
    st.caption(f"Tokens: {total['input_tokens']:,} in / {total['output_tokens']:,} out · estimated cost ${cost(total):.3f}")
    st.markdown(md)

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for set_id, out in outputs.items():
            z.writestr(f"outputs/{run_name}/{set_id}.json", json.dumps(out, indent=2))
        z.writestr(f"results/{run_name}.md", md)
    st.download_button("Download outputs and report (.zip)", buf.getvalue(), file_name=f"{run_name}.zip")


if page == "Prepare for my appointment":
    prepare_page()
else:
    evaluation_page()
