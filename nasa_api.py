import requests

class NasaClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov/planetary/apod"

    def get_apod_data(self, date: str = None) -> dict:
        params = {"api_key": self.api_key}
        if date:
            params["date"] = date

        response = requests.get(self.base_url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()

    def get_image_bytes(self, url: str) -> bytes:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.content