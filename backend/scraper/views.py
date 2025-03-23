# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import scrapedModel
# from .serializers import scrapedSerializer
# import requests
# from bs4 import BeautifulSoup

# @api_view(['POST'])
# def scrape_site(request):
#   url = request.data.get('url')
#   if not url:
#     return Response({'error': 'No URL provided'},status=400)
  
#   try:
#     response = requests.get(url)
#     response.raise_for_status()
#     soup = BeautifulSoup(response.content,'html.parser')
#     text = soup.get_text()

#     # Save to database
#     scraped_data = scrapedModel.objects.create(url=url,content=text)
#     serializer = scrapedSerializer(scraped_data)

#     return Response({'data': serializer.data})
  
#   except Exception as e:
#     return Response({'error': str(e)},status=500)

import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import scrapedModel
from .serializers import ScrapeSerializer, ScrapeRequestSerializer
from .scraper_logic import WebScraper

logger = logging.getLogger(__name__)

class ScrapeSiteView(APIView):
    def post(self, request):
        serializer = ScrapeRequestSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            try:
                # Scrape content
                scraped_content = WebScraper.scrape(url)

                # Save to database (optional)
                scraped_data = scrapedModel.objects.create(url=url, content=scraped_content)
                response_serializer = ScrapeSerializer(scraped_data)
                
                return Response({'data': response_serializer.data}, status=status.HTTP_200_OK)
            except Exception as e:
                logger.error(f"Scraping failed: {str(e)}")
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
