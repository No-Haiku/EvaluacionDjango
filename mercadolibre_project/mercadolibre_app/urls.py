from django.urls import path
from . import views

urlpatterns = [
    path('top-users/', views.top_users, name='top_users'),
    path('expensive-listings/', views.expensive_listings, name='expensive_listings'),
]
