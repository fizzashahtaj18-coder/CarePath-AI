"""Split documents into numbered chunks (FR-2.1).

Every chunk gets a stable ID like "D2-C3" (document 2, chunk 3). The LLM must cite these IDs,
and code later checks that each quoted sentence really exists in its chunk.
"""
import re
from dataclasses import dataclass

SYNTHETIC_BANNER = "SYNTHETIC TEST DOCUMENT. NOT A REAL PATIENT."


@dataclass
class Chunk:
    chunk_id: str   # e.g. "D2-C3"
    doc_id: str     # e.g. "D2"
    text: str


def split_sentences(line):
    """Split a line into sentences. Keeps short note-style lines whole."""
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"(])", line.strip())
    return [p.strip() for p in parts if p.strip()]


def chunk_document(doc_id, text):
    """Return the document's chunks: one per sentence (or per line for shorthand notes)."""
    chunks = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line == SYNTHETIC_BANNER:
            continue
        for sentence in split_sentences(line):
            chunks.append(Chunk(f"{doc_id}-C{len(chunks) + 1}", doc_id, sentence))
    return chunks


def chunk_documents(documents):
    """documents: list of dicts {"id": "D1", "title": "...", "text": "..."}"""
    out = {}
    for d in documents:
        out[d["id"]] = chunk_document(d["id"], d.get("text", ""))
    return out
