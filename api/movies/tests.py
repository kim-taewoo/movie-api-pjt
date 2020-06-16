from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.utils import timezone
from .models import Movie, Actor, Director, Review
from users.models import User

# from pprint import pprint

class MovieTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.test_user = User.objects.create_user(username='testuser', password='testpassword')

        for i in range(1, 10):
            actor_data = { 'name': f'actor{i}' }
            director_data = { 'name': f'director{i}' }
            Actor.objects.create(**actor_data)
            Director.objects.create(**director_data)

        for i in range(1, 30):
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
                self.test_movie.actors.add(*Actor.objects.filter(id__in=list(range(1, 10))))
                self.test_movie.directors.add(*Director.objects.filter(id=i%10))
            else:
                test_movie = Movie.objects.create(**data)
                test_movie.actors.add(*Actor.objects.filter(id__in=list(range(1, 10))))
                test_movie.directors.add(*Director.objects.filter(id=i%10))

        for i in range(1, 6):
            data = {
                'rating': i,
                'content': f'message{i}',
                'creator': self.test_user,
                'movie': self.test_movie,
            }
            if i == 1:
                self.test_review = Review.objects.create(**data)
            else:
                test_review = Review.objects.create(**data)
                if i > 3:
                    test_review.likes.add(self.test_user)
        
        self.movie_api_url = reverse('movies:movie_api')
        self.movie_detail_api_url = reverse('movies:movie_detail_api', kwargs={'movie_id': self.test_movie.id})
        self.movie_recommend_url = reverse('movies:movie_recommend', kwargs={'movie_id': self.test_movie.id})
        self.review_api_url = reverse('movies:review_api', kwargs={'movie_id': self.test_movie.id})
        self.review_detail_api_url = reverse('movies:review_detail_api', kwargs={'review_id': self.test_review.id })
        self.like_review_url = reverse('movies:like_review', kwargs={'review_id': self.test_review.id })
        
        self.client.force_authenticate(user=self.test_user)


    def test_get_movies(self):
        response = self.client.get(self.movie_api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)

    def test_get_reviews(self):
        response = self.client.get(self.review_api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertFalse(response.data[0]['is_liked'])
        self.assertTrue(response.data[4]['is_liked'])

    def test_like_review(self):
        response = self.client.get(self.like_review_url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.review_detail_api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['is_liked'])