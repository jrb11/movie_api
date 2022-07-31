from string import printable
import requests
from django.shortcuts import render
from .models import movie_data
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Movies_View_Serializer
import json

# Create your views here.

# ------------------ Part -1 ---------------------
class Movies_View_List(viewsets.ViewSet):
    serializers_class = Movies_View_Serializer

    def list(self, request):
        queryset = movie_data.objects.all()
        serializer = Movies_View_Serializer(queryset, many=True)
        return Response(serializer.data)

class Movies_View_By_ID(viewsets.ViewSet):
    serializers_class = Movies_View_Serializer

    def retrieve(self, request, id=None):
        try:
            print("ID:", id)
            movie_obj = movie_data.objects.get(id=id)
            serializer = Movies_View_Serializer(movie_obj)
        except Exception as error:
            return Response({"response": False, "message": str(error)},  status=400)
        return Response(serializer.data)

class Movies_View_By_Year(viewsets.ViewSet):
    serializers_class = Movies_View_Serializer

    def list(self, request, released_year=None):
        try:
            print("Year:", released_year)
            movie_obj = movie_data.objects.filter(released_year=released_year)
            serializer = Movies_View_Serializer(movie_obj, many=True)

        except Exception as error:
            return Response({"response": False, "message": str(error)},  status=400)
        return Response(serializer.data)

class Movies_View_By_Rating(viewsets.ViewSet):
    serializers_class = Movies_View_Serializer

    def list(self, request, ratings=None):
        try:
            print("Rating:", ratings)
            movie_obj = movie_data.objects.get(ratings=ratings)
            serializer = Movies_View_Serializer(movie_obj)

        except Exception as error:
            return Response({"response": False, "message": str(error)},  status=400)
        return Response(serializer.data)

class Movies_View_By_Genre(viewsets.ViewSet):
    serializers_class = Movies_View_Serializer

    def list(self, request, genres=None):
        try:
            print("Genre:", genres)
            movie_obj = movie_data.objects.filter(genres__icontains=genres.lower())
            serializer = Movies_View_Serializer(movie_obj, many=True)

        except Exception as error:
            return Response({"response": False, "message": str(error)},  status=400)
        return Response(serializer.data)


# ------------------ Part -2 ---------------------

class Movies_View_By_Title(viewsets.ViewSet):
    serializers_class = Movies_View_Serializer

    def list(self, request, title=None):
        try:
            print("Title:", title)
            movie_obj = movie_data.objects.filter(title__icontains=title).exists()

            if movie_obj:
                movie_obj = movie_data.objects.get(title__icontains=title)
                serializer = Movies_View_Serializer(movie_obj)
            else:
                print(f'No {title} found')
                url = 'http://www.omdbapi.com/?apikey=????????&t=%s'%title
                response = requests.get(url)
                data = response.json()
                new_movie_obj = movie_data()
                new_title = data['Title']
                new_movie_obj.title = data['Title']
                new_movie_obj.released_year = data['Year']
                new_movie_obj.ratings = data['imdbRating']
                new_movie_obj.genres = data['Genre']
                new_movie_obj.save()
             
                movie_obj = movie_data.objects.get(title__icontains=new_title)
                serializer = Movies_View_Serializer(movie_obj)

        except Exception as error:
            return Response({"response": False, "message": str(error)},  status=400)
        return Response(serializer.data)