from fastapi import APIRouter
from api.src.schemas import ItemModelRequest, ItemModelResponse
from api.src.controllers import SearchControllers


router = APIRouter()
searchControllers = SearchControllers()


@router.post('/related-search', response_model=ItemModelResponse)
def search(data: ItemModelRequest):
    response = searchControllers.search(data.category, data.search)
    return response

@router.get('/')
def home():
    return {'message': 'análise-de-markov'}
