# API GUIDE

- `api/v1/movies/` : 영화 가져오기, 영화 목록 업데이트
- `api/v1/movies/<int:movie_id>/` : 영화 상세 가져오기
- `api/v1/movies/<int:movie_id>/reviews/` : 리뷰 생성, 리뷰 모두 가져오기
- `api/v1/movies/<int:movie_id>/reviews/<int:review_id>/` : 리뷰 수정, 리뷰 삭제