from django.urls import path

from intro import views

urlpatterns = [
    path('first_page/',views.hello, name='first-page'),
    path('show_name/',views.name, name='show-name'),
    path('list_of_cars/',views.cars, name='list-of-cars'),
    path('motorcycles/', views.list_of_motorcycles, name='motorcycles'),
]

# PREFIXUL ESTE UNIC.
# NAME-Ul ESTE UNIC.
# FIECARE PATH VA AVEA O FUNCTIE SAU O CLASA.