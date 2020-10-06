from pydantic import BaseModel


class ItemModelRequest(BaseModel):
    search: str
    category: str


class ItemModelResponse(BaseModel):
    text: str