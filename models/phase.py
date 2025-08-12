from pydantic import BaseModel, Field


class Phase(BaseModel):
    id: int = Field(..., ge=1, le=5)
    active: bool
    duration: int
