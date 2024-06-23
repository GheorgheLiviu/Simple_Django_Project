from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
@login_required
def hello(request):
    return HttpResponse('Hello world!')

@login_required()
def name(request):
    return HttpResponse('Liviu')

@login_required
def cars(request):
    list_cars = {
        "all_cars": [
            {
                'brand': 'VW',
                'model': '6',
                'year': 2020,
            },
            {
                'brand': 'BMW',
                'model': 530,
                'year': 2021,
            },
            {
                'brand': 'Audi',
                'model': 'A6',
                'year': 2023
            }
        ]
    }

    return render(request, 'intro/list_of_cars.html', list_cars)

@login_required
def list_of_motorcycles(request):
    list_motorcycles = {
        "motorcycles": [
            {
                "brand": "Kawasaki",
                "speed": 190,
                "year": 2022,
                "model": "Z650"
            },
            {
                "brand": "Honda",
                "speed": 260,
                "year": 2003,
                "model": "Hornet"
            },
            {
                "brand": "BMW",
                "speed": 220,
                "year": 2023,
                "model": "GS1250"
            }

        ]
    }
    return render(request, 'intro/motorcycles.html', list_motorcycles)
