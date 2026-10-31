"""The structure the LLM must return (FR-2.3, FR-2.4).

Used twice: as the tool's JSON schema sent to the model, and to validate what comes back.
"""
from typing import List, Literal
from pydantic import BaseModel, Field

TOPIC_IDS = Literal[
    "photo_id", "insurance_card", "referral_on_file", "previous_records", "medication_list",
    "test_preparation", "arrival_time", "location_parking", "forms", "reschedule_cancel",
]


class Citation(BaseModel):
    chunk_id: str = Field(description="Chunk ID like 'D2-C3', exactly as shown in the documents")
    quote: str = Field(description="The exact words copied from that chunk. Do not paraphrase.")


class Item(BaseModel):
    text: str = Field(description="One action in plain language. Medical instructions: keep the original wording.")
    category: Literal["Bring", "Do", "Before-date"]
    due_date: str | None = Field(default=None, description="YYYY-MM-DD only if the documents give or imply one exact date; otherwise null")
    citations: List[Citation] = Field(min_length=1)
    medical_instruction: bool = Field(description="True for anything about medication, eating/drinking, test or procedure preparation")


class Conflict(BaseModel):
    topic: str = Field(description="What the documents disagree about, e.g. 'arrival time'")
    citations: List[Citation] = Field(min_length=2, description="Every disagreeing version, one citation each")


class ChecklistOutput(BaseModel):
    no_instructions_found: bool = Field(description="True if the documents contain no appointment preparation instructions for the patient")
    items: List[Item] = Field(default_factory=list)
    conflicts: List[Conflict] = Field(default_factory=list)
    covered_topics: List[TOPIC_IDS] = Field(default_factory=list, description="Topics the documents DO mention (see the topic list)")
