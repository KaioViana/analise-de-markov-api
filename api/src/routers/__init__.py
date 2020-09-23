from fastapi import APIRouter
from schemas import ItemModelRequest, ItemModelResponse

router = APIRouter()

@router.post('/related-search', response_model=ItemModelResponse)
async def search(data: ItemModelRequest):
    return None
