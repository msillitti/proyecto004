from django.urls import path
from   inicar.views import primera_vista, home, vista2, template_1

urlpatterns = [
    path('primera-vista/', primera_vista),
    path('', home),
    path('vista2/<dato>/', vista2),
    path('template_1/', template_1),
]