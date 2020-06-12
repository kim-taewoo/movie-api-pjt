from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieAPI.as_view(), name='movie_api'),
    path('<int:movie_id>/', views.MovieDetailAPI.as_view(), name='movie_detail_api'),
    path('<int:movie_id>/reviews/', views.ReviewAPI.as_view(), name='review_api'),
    path('reviews/<int:review_id>/', views.ReviewDetailAPI.as_view(), name='review_detail_api'),
]
