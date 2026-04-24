import httpx
from typing import Optional

# These are your local files
from models import SearchResultsModel, SpecificItemDetailsModel
from constants import BASE_URL


class MovieBoxV2Engine:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Platform": "pc",
            "Referer": "https://moviebox.ph"
        }
        self.base_url = "https://h5-api.aoneroom.com"

    async def search(self, query: str, page: int = 1) -> SearchResultsModel:
        url = f"{self.base_url}/wefeed-h5api-bff/subject/search"
        params = {
            "keyword": query,
            "page": page,
            "per_page": 20,
            "type": "all"
        }

        async with httpx.AsyncClient(headers=self.headers) as client:
            response = await client.get(url, params=params)
            return SearchResultsModel(**response.json())

    async def get_details(self, detail_path: str) -> SpecificItemDetailsModel:
        url = f"{self.base_url}/wefeed-h5api-bff/detail"
        params = {"detailPath": detail_path}

        async with httpx.AsyncClient(headers=self.headers) as client:
            response = await client.get(url, params=params)
            return SpecificItemDetailsModel(**response.json())

    async def get_homepage(self):
        url = f"{self.base_url}/wefeed-h5api-bff/home?host=moviebox.ph"

        async with httpx.AsyncClient(headers=self.headers) as client:
            response = await client.get(url)
            return response.json()

    async def get_suggestions(self, query: str):
        url = f"{self.base_url}/wefeed-h5api-bff/subject/search-suggest"
        params = {"keyword": query}

        async with httpx.AsyncClient(headers=self.headers) as client:
            response = await client.get(url, params=params)
            return response.json()

    async def get_category(self, category_id: str, page: int = 1):
        url = f"{self.base_url}/wefeed-h5api-bff/home/category"
        params = {"genreId": category_id, "page": page}

        async with httpx.AsyncClient(headers=self.headers) as client:
            response = await client.get(url, params=params)
            return response.json()
