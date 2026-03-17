from pydantic import BaseModel

class InterviewCreate(BaseModel):
    role: str
    level: str