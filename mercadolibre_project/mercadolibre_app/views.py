from django.shortcuts import render
from .models import User, Listing

import requests
from django.shortcuts import render

def top_users(request):
   
 
api_users_url = "https://api.mercadolibre.com/sites/MLA/search?category=MLA352679"

try:

    response_users = requests.get(api_users_url)
    if response_users.status_code == 200:
        users_data = response_users.json()

       
        sorted_users = sorted(users_data["users"], key=lambda x: x["units_sold"], reverse=True)

       
        top_users_data = sorted_users[:5]

        return render(request, 'mercadolibre_app/top_users.html', {'top_users': top_users_data})
    else:
        return render(request, 'mercadolibre_app/error.html', {'error_message': 'Error al obtener datos de usuarios'})
except requests.exceptions.RequestException as e:
    return render(request, 'mercadolibre_app/error.html', {'error_message': str(e)})





import requests
from django.shortcuts import render

def expensive_listings(request):
    
    api_listings_url = "https://api.mercadolibre.com/sites/MLA/search?category=MLA352679"

    try:
     
        response_listings = requests.get(api_listings_url)
        if response_listings.status_code == 200:
            listings_data = response_listings.json()

            
            sorted_listings = sorted(listings_data["listings"], key=lambda x: x["price"], reverse=True)

            
            expensive_listings_data = sorted_listings[:20]

            return render(request, 'mercadolibre_app/expensive_listings.html', {'expensive_listings': expensive_listings_data})
        else:
            return render(request, 'mercadolibre_app/error.html', {'error_message': 'Error al obtener datos de publicaciones'})
    except requests.exceptions.RequestException as e:
        return render(request, 'mercadolibre_app/error.html', {'error_message': str(e)})
