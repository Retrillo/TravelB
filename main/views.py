from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request , "main/about.html")

def hotels(request):
    return render(request , "main/hotels.html")

def tours(request):
    return render(request , "main/tours.html")

def flights(request):
    return render(request , "main/flights.html")

def connection(request):
    return render(request , "main/connection.html")

def bag(request):
    return render(request , "main/bag.html")




