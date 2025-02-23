# import requests
# from bs4 import BeautifulSoup

# class WebScraper:
#     @staticmethod
#     def scrape(url: str) -> str:
#         try:
#             response = requests.get(url)
#             response.raise_for_status()  # Check if request was successful
#             soup = BeautifulSoup(response.content, 'html.parser')
#             text = soup.get_text(separator='\n')
#             return text
#         except requests.exceptions.RequestException as e:
#             raise Exception(f"Failed to fetch data: {str(e)}")

import requests
from bs4 import BeautifulSoup

class WebScraper:
    @staticmethod
    def scrape(url: str) -> str:
        try:
            headers = {
                'User-Agent': (
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/112.0.0.0 Safari/537.36'
                )
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Check if request was successful
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text(separator='\n', strip=True)
            return text
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch data: {str(e)}")
