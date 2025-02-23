# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import ScrappedModel
# from .serializers import ScrappedSerializer
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
#     scrapped_data = ScrappedModel.objects.create(url=url,content=text)
#     serializer = ScrappedSerializer(scrapped_data)

#     return Response({'data': serializer.data})
  
#   except Exception as e:
#     return Response({'error': str(e)},status=500)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ScrappedModel
from .serializers import ScrapeSerializer, ScrapeRequestSerializer
from .scrapper_logic import WebScraper

class ScrapeSiteView(APIView):
    def post(self, request):
        serializer = ScrapeRequestSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            try:
                scraped_content = WebScraper.scrape(url)

                # Save to database (optional)
                scraped_data = ScrappedModel.objects.create(url=url, content=scraped_content)
                response_serializer = ScrapeSerializer(scraped_data)
                
                return Response({'data': response_serializer.data}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
