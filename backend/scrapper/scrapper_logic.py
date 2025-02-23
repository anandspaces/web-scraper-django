import requests
from bs4 import BeautifulSoup

class WebScraper:
    @staticmethod
    def scrape(url: str) -> str:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if request was successful
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text(separator='\n')
            return text
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch data: {str(e)}")
