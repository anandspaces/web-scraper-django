from django.urls import path
from .views import ScrapeSiteView

urlpatterns = [
  # path('scrape/',scrape_site,name='scrape_site'),
  path('scrape/',ScrapeSiteView.as_view(),name='scrape_site'),
]