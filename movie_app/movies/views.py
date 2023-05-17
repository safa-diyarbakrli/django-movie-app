from django.shortcuts import render
from .models import Category, Movie
category_list = ["comedy","mystery","action","drama"]
movie_list = [
    {
        "id": 1, 
        "movie_name": "sherlock holmes",
        "description": "movie 1 description",
        "picture": "1.jpeg",
        "mainpage": True
    },
    {
        "id": 2,
        "movie_name": "knives out ",
        "description": "movie 2 description",
        "picture": "2.jpeg",
        "mainpage": True
    },

    {
        "id": 3,
        "movie_name": "deadpool 2",
        "description": "movie 3 description",
        "picture": "3.jpeg",
        "mainpage": False
    },
    {
        "id": 4,
        "movie_name": "jojo rabbit",
        "description": "movie 4 description",
        "picture": "4.jpeg" ,
        "mainpage": False
    } 
]
  
def home(request):
    data = {
        "categories": Category.objects.all(),
        "movies": Movie.objects.filter(mainpage=True)
        }
    return render(request, "index.html", data)

def movies(request):
    data = {
        "categories": Category.objects.all(),
        "movies": Movie.objects.all()
        }
    return render(request, "movies.html", data)

    
def movie_details(request, id):
    data = {
        "movie": Movie.objects.get(id=id)
        }
    return render(request, "details.html", data)


    







