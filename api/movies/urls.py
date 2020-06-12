from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieAPI.as_view(), name='movie_api'),
    path('<int:movie_id>/', views.MovieDetailAPI.as_view(), name='movie_detail_api'),
]
