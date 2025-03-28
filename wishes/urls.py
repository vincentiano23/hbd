from django.urls import path
from wishes.views import wish_response, home

urlpatterns = [
    path('', home, name='home'),
    path('wish/', wish_response, name='wish_response'),
    
]
