from pydantic import BaseModel


class ItemModelRequest(BaseModel):
    search: str
    category: str


class ItemModelResponse(BaseModel):
    text: str
    corpus_words: list
    distinct_words: list