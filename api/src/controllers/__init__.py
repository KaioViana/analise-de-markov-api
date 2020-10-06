from models import SearchModels


class SearchControllers:
    def __init__(self):
        self.searchModels = SearchModels()


    def search(self, category, search):
        return self.searchModels.search(category, search)