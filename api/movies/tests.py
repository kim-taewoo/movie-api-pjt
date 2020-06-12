from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.utils import timezone
from .models import Movie
from users.models import User

# from pprint import pprint

class MovieTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.test_user = User.objects.create_user(username='testuser', password='testpassword')

        for i in range(1, 10):
            data = {
                'title': f'movie{i}',
                'sub_title': f'm{i}',
                'poster': f'url{i}.com',
                'rating': 10.0,
                'pub_date': timezone.now(),
                'runtime': 200,
                'overview': f'overview {i}',
                'audits': f'12세 관람가',
                'movie_cd': i,
                'audi_cnt': 1000000,
            }
            if i == 1:
                self.test_movie = Movie.objects.create(**data)
            else:
                Movie.objects.create(**data)

        
        self.movie_api_url = reverse('movies:movie_api')
        self.movie_detail_api_url = reverse('movies:movie_detail_api', kwargs={'movie_id': self.test_movie.id})
        self.review_api_url = reverse('movies:review_api', kwargs={'movie_id': self.test_movie.id})
        
        self.client.force_authenticate(user=self.test_user)


    def test_get_movies(self):
        response = self.client.get(self.movie_api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 9)
