import requests
from utils.config import Config

class APIClient:

    @staticmethod
    def get(endpoint):
        return requests.get(f"{Config.API_BASE_URL}{endpoint}")

    @staticmethod
    def post(endpoint, payload):
        return requests.post(f"{Config.API_BASE_URL}{endpoint}", json=payload)
