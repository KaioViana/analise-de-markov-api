from pydantic import BaseModel


class ItemModelRequest(BaseModel):
    search: str
    box: str


class ItemModelResponse(BaseModel):
    text: str