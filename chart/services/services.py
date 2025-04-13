import json
import requests
from django.conf import settings
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from django.core.cache import cache

load_dotenv()
api_key = os.getenv('API_KEY')



today = datetime.now().strftime("%Y-%m-%d")  
BASE_URL = "https://openpricengine.com/api/v0.3/"

def egg_pricess_history(store, productname, start_date, end_date):
    cache_key = f"egg_prices_{store}_{productname}_{start_date}_{end_date}"
    
    cached_data = cache.get(cache_key)
    if cached_data:
        print("✅ Serving from cache")
        return cached_data



    url = f"{BASE_URL}all/query"

    headers = {
        'Authorization' : api_key,
        'accept': 'application/json',
    }

    params = {
        'stores': store,
        'productname': productname,
        'start_date': start_date,
        'end_date': end_date,
        'currency' : 'USD'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            cache.set(cache_key, data, timeout=3600)  # Store in cache for 1 hour
            return data
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

    

eggs= egg_pricess_history('pnp', 'eggs', '2025-01-12', today)




    



    



