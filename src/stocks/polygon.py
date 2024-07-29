from django.conf import settings
from polygon import RESTClient

client = RESTClient(api_key=settings.POLYGON_API_KEY)
