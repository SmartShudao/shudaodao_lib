from pydantic import BaseModel

class ResponseSignedModel(BaseModel):
    key: int
    url: str
