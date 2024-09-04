from langchain_core.pydantic_v1 import BaseModel, validator

class ModelOutput(BaseModel):
    reasoning: str
    sentiment_score: int
    politeness_score: int

    @validator('sentiment_score')
    def sentiment_score_must_be_in_range(cls, v):
        if not -100 <= v <= 100:
            raise ValueError('sentiment_score must be between -100 and 100')
        return v

    @validator('politeness_score')
    def politness_score_must_be_positive(cls, v):
        if not -100 <= v <= 100:
            raise ValueError('politeness_score must be between -100 and 100')
        return v
