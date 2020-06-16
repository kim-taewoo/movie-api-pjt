import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from api.pagination import BasicPagination, PaginationHandlerMixin
from django.conf import settings
from .models import Movie, Actor, Director, Genre, Country, Review
from .serializers import MovieSerializer, ReviewSerializer, ReviewCreateSerializer
from django.db.models import Q

def get_movie(movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        return movie
    except Movie.DoesNotExist:
        return None

def get_review(review_id):
    try:
        review = Review.objects.get(id=review_id)
        return review
    except Review.DoesNotExist:
        return None


# Create your views here.

class MovieAPI(APIView, PaginationHandlerMixin):
    permission_classes = [AllowAny]
    pagination_class = BasicPagination
    serializer_class = MovieSerializer
    
    def get_kobis_url(self, key, movieCd):
        KOBIS_DETAIL_URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
        return KOBIS_DETAIL_URL

    def get_naver_url(self, query):
        NAVER_URL = f'https://openapi.naver.com/v1/search/movie.json?query={query}'
        return NAVER_URL

    def get(self, request):
        order_by = request.GET.get('order_by', None)
        if order_by:
            movies = Movie.objects.order_by(order_by)
        else:
            movies = Movie.objects.all()
            
        page = self.paginate_queryset(movies)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(movies, many=True)
        # pp(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        NAVER_ID = settings.NAVER_ID
        NAVER_SECRET = settings.NAVER_SECRET
        TMDB_KEY = settings.TMDB_KEY
        KOBIS_KEY = settings.KOBIS_KEY

        naver_headers = {
            'X-Naver-Client-Id': NAVER_ID,
            'X-Naver-Client-Secret': NAVER_SECRET,
        }

        year = 1
        month = 2

        for y in range(0, year):
            for m in range(1, month):

                KOBIS_URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={KOBIS_KEY}&targetDt=202{y}0{m}01'
                
                response = requests.get(KOBIS_URL)

                tmp = response.json()
                
                results = tmp['boxOfficeResult']['dailyBoxOfficeList']

                for result in results:
                    movie_cd = result['movieCd']
                    audi_cnt = int(result['audiCnt'])
                    try:
                        movie = Movie.objects.get(movie_cd=movie_cd)
                        if movie.audi_cnt < audi_cnt:
                            movie.audi_cnt = audi_cnt
                            movie.save()
                        continue
                    except Movie.DoesNotExist:
                        movie_response = requests.get(self.get_kobis_url(KOBIS_KEY, result['movieCd']))
                        movie_results = movie_response.json()['movieInfoResult']['movieInfo']
                        actors_res = movie_results['actors']
                        directors_res = movie_results['directors']
                        nations_res = movie_results['nations']
                        genres_res = movie_results['genres']
                        actors = []
                        directors = []
                        nations = []
                        genres = []
                        audits = movie_results['audits'][0]['watchGradeNm']
                        title = movie_results['movieNm']
                        sub_title = movie_results['movieNmEn']
                        dt = movie_results['openDt']
                        runtime = movie_results['showTm']
                        pub_date = dt[:4] + '-' + dt[4:6] + '-' + dt[6:]
                        overview = ''
                        naver_response = requests.get(self.get_naver_url(
                            title), headers=naver_headers).json()['items'][0]
                        rating = naver_response['userRating']
                        # poster = naver_response['image']
                        link_url = naver_response['link'].strip()
                        poster_url = link_url.split('=')
                        poster_tmp = 'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode={}'.format(poster_url[1])
                        poster_response = requests.get(poster_tmp)
                        html = poster_response.text
                        soup = BeautifulSoup(html, 'lxml')
                        horizontal_poster = None
                        tmp = soup.select('#targetImage')
                        poster = tmp[0].get('src')
                        #targetImage
                        overview_response = requests.get(link_url)
                        html = overview_response.text
                        soup = BeautifulSoup(html, 'lxml')
                        overview = soup.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div > p')

                        horizontal_url = 'http://www.cgv.co.kr/search/stillcut.aspx?query={}'.format(title)
                        horizontal_response = requests.get(horizontal_url)
                        html = horizontal_response.text
                        soup = BeautifulSoup(html, 'lxml')
                        horizontal_poster = None
                        tmp = soup.select('#contents > div > div.cols-content > div.col-detail > div > div.sect-stillcut > ul > li:nth-child(9) > a > img')
                        if tmp:
                            horizontal_poster = tmp[0].get('src')

                        for i in overview:
                            overview = i.text

                        for actor in actors_res:
                            try:
                                actress = Actor.objects.get(name=actor['peopleNm'])
                            except Actor.DoesNotExist:
                                actress = Actor.objects.create(name=actor['peopleNm'])
                            actors.append(actress)  

                        for direc in directors_res:
                            try:
                                director = Director.objects.get(name=direc['peopleNm'])
                            except Director.DoesNotExist:
                                director = Director.objects.create(name=direc['peopleNm'])
                            directors.append(director)

                        for g in genres_res:
                            try:
                                genre = Genre.objects.get(name=g['genreNm'])
                            except Genre.DoesNotExist:
                                genre = Genre.objects.create(name=g['genreNm'])
                            genres.append(genre)

                        for country in nations_res:
                            try:
                                nation = Country.objects.get(name=country['nationNm'])
                            except Country.DoesNotExist:
                                nation = Country.objects.create(name=country['nationNm'])
                            nations.append(nation)

                        created_movie = Movie.objects.create(
                            title=title,
                            sub_title=sub_title,
                            poster=poster,
                            horizontal_poster=horizontal_poster,
                            rating=rating,
                            pub_date=pub_date,
                            runtime=runtime,
                            overview=overview,
                            audits=audits,
                            movie_cd=movie_cd,
                            audi_cnt=audi_cnt
                        )

                        created_movie.actors.add(*actors)
                        created_movie.directors.add(*directors)
                        created_movie.nations.add(*nations)
                        created_movie.genres.add(*genres)

        return Response(status=status.HTTP_201_CREATED)


class MovieDetailAPI(APIView):
    
    def get(self, request, movie_id):
        movie = get_movie(movie_id)
        if not movie:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieRecommendation(APIView):
    
    def get(self, request, movie_id):
        movie = get_movie(movie_id)
        if not movie:
            return Response(status=status.HTTP_404_NOT_FOUND)
        actors = movie.actors.all()[:10]
        genres = movie.genres.all()
        # movies = Movie.objects.filter(actors__in=actors).exclude(title=movie.title)[:4]
        movies = Movie.objects.filter(Q(actors__in=actors)|Q(genres__in=genres)).exclude(title=movie.title).filter().distinct()[:4]
        if len(movies) < 4:
            movies = Movie.objects.all()[:4]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewAPI(APIView, PaginationHandlerMixin):
    
    def get(self, request, movie_id):
        user = request.user
        movie = get_movie(movie_id)
        if not movie:
            return Response(status=status.HTTP_404_NOT_FOUND)
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, movie_id):
        user = request.user
        movie = get_movie(movie_id)
        if not movie:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(creator=user, movie=movie)
            if review:
                new_serializer = ReviewSerializer(review, context={"request":request})
                return Response(new_serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailAPI(APIView):

    def put(self, request, review_id):
        user = request.user
        review = get_review(review_id)
        if not review:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewCreateSerializer(review, data=request.data, context={"request":request})
        if serializer.is_valid():
            review = serializer.save()
            if review:
                new_serializer = ReviewSerializer(review)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, review_id):
        user = request.user
        review = get_review(review_id)
        if not review:
            return Response(status=status.HTTP_404_NOT_FOUND)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeReview(APIView):

    def get(self, request, review_id):
        user = request.user
        review = get_review(review_id)
        if not review:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if user in review.likes.all():
            review.likes.remove(user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            review.likes.add(user)
            return Response(status=status.HTTP_201_CREATED)


class UnlikeReview(APIView):

    def get(self, request, review_id):
        user = request.user
        review = get_review(review_id)
        if not review:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if user in review.unlikes.all():
            review.unlikes.remove(user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            review.unlikes.add(user)
            return Response(status=status.HTTP_201_CREATED)
