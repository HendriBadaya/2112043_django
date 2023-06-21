from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home),
    path("profile/",views.profile),
    path("balikpapan/",views.balikpapan),
]

    
