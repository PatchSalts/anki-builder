import requests
import json

def lookup_japanese(text: str) -> list[dict]:
    response = requests.get("https://jisho.org/api/v1/search/words?keyword=" + text)
    response.raise_for_status()
    data = json.loads(response.text)
    return data["data"]