from pydantic import BaseModel


class Stats(BaseModel):
    title: str
    body: str
