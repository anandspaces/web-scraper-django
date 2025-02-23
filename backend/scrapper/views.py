from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ScrappedModel
from .serializers import ScrappedSerializer
import requests
from bs4 import BeautifulSoup

@api_view(['POST'])
def scrape_site(request):
  url = request.data.get('url')
  if not url:
    return Response({'error': 'No URL provided'},status=400)
  
  try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content,'html.parser')
    text = soup.get_text()

    # Save to database
    scrapped_data = ScrappedModel.objects.create(url=url,content=text)
    serializer = ScrappedSerializer(scrapped_data)

    return Response({'data': serializer.data})
  
  except Exception as e:
    return Response({'error': str(e)},status=500)