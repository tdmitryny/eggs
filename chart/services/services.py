import requests
from django.conf import settings
from datetime import datetime, timedelta
import tradingeconomics as te


API_KEY = settings.API_KEY  

def egg_pricess_history():
    headers = {
        'Authorization' : API_KEY,
        'accept': 'application/json',
    }

    params = {
        'store': 'pnp',
        'productname': 'egg',
        'start_date': '2025-01-01',
        'end_date': '2025-04-08',
        'currency' : 'Default'
    }


    url = "https://openpricengine.com/api/v0.3/"


