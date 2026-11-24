from typing import Literal
from pydantic import BaseModel, Field

class Triage(BaseModel):
    category: Literal["billing", "shipping", "other"]
    priority: int = Field(ge=0, le=6)

def parse_answer(answer: str) -> Triage:
    return Triage.model_validate_json(answer)