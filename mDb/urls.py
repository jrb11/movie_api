from django.contrib import admin
from django.urls import path, register_converter
from .import views


class FloatConverter:
    regex = '[\d\.\d]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return '{}'.format(value)
        
register_converter(FloatConverter, 'float')


urlpatterns = [

    path('movies/list/', views.Movies_View_List.as_view({'get': 'list'})),
    path('movies/id/<int:id>/', views.Movies_View_By_ID.as_view({'get': 'retrieve'})),
    path('movies/year/<int:released_year>/', views.Movies_View_By_Year.as_view({'get': 'list'})),
    path('movies/rating/<float:ratings>/', views.Movies_View_By_Rating.as_view({'get': 'list'})),
    path('movies/genre/<str:genres>/', views.Movies_View_By_Genre.as_view({'get': 'list'})),

    path('movies/title/<str:title>/', views.Movies_View_By_Title.as_view({'get': 'list'})),
   
]