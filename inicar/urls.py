from django.urls import path
from   inicar.views import primera_vista, home
urlpatterns = [
    path('primera-vista/', primera_vista),
    path('', home),
    
]