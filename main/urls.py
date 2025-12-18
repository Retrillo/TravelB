from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='home'),
    path('about', views.about, name='about'),
    path('hotels', views.hotels, name='hotels'),
    path('tours', views.tours, name='tours'),
    path('flights', views.flights, name='flights'),
    path('bag', views.bag, name='bag'),

]


