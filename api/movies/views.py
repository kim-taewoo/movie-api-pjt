import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.conf import settings
from .models import Movie, Actor, Director, Genre, Country
from .serializers import MovieSerializer


# Create your views here.

class MovieAPI(APIView):
    permission_classes = [AllowAny]

    def get_kobis_url(self, key, movieCd):
        KOBIS_DETAIL_URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
        return KOBIS_DETAIL_URL

    def get_naver_url(self, query):
        NAVER_URL = f'https://openapi.naver.com/v1/search/movie.json?query={query}'
        return NAVER_URL


    def get(self, request):
        order_by = request.GET.get('order_by', None)
        if order_by:
            movies = Movie.objects.order_by(order_by)[:10]
        else:
            movies = Movie.objects.all()[:10]

        serializer = MovieSerializer(movies, many=True)

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

        for y in range(1):
            for m in range(7):

                KOBIS_URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={KOBIS_KEY}&targetDt=20200{m}01'
                
                response = requests.get(KOBIS_URL)

                results = response.json()['boxOfficeResult']['dailyBoxOfficeList']

                for result in results[:2]:
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
                        naver_response = requests.get(self.get_naver_url(title), headers=naver_headers).json()['items'][0]
                        rating = naver_response['userRating']
                        poster = naver_response['image']
                        link_url = naver_response['link'].strip()
                        overview_response = requests.get(link_url)
                        html = overview_response.text
                        soup = BeautifulSoup(html, 'lxml')
                        overview = soup.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div > p')
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

