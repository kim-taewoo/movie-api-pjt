## Movie API

     
### `/api/v1/movies/` ( 영화 가져오기 )

#### 높은 평점순
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | GET | 200(성공), 401(인증실패) | True | | `?order_by=-rating` |

#### 낮은 평점순
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | GET | 200(성공), 401(인증실패) | True | | `?order_by=rating` |

#### 최근 영화순
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | GET | 200(성공), 401(인증실패) | True | | `?order_by=-pub_date` |

#### 관객수순
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | GET | 200(성공), 401(인증실패)| True | | `?order_by=-audi_cnt` |

  - 리턴 데이터 타입
    ```js
    [
      {
        id: Number,
        title: String,  // 한글 타이틀
        sub_title: String,  // 영어 타이틀
        poster: String,
        rating: Float,
        pub_date: 'YYYY-MM-DD',
        runtime: Number,
        overview: String,
        audits: String, // 12세 관람가, 15세 관람가 등
        audi_cnt: Number, // 관객수
        genres: [
          {
            id: Number,
            name: String,
          },
          // ...
        ],
        actors: [
          {
            id: Number,
            name: String,
          },
          // ...
        ],
        directors: [
          {
            id: Number,
            name: String,
          },
          // ...
        ],
        nations: [
          {
            id: Number,
            name: String,
          },
          // ...
        ],
      },
      // ...
    ]
    ```

<br />

### `/api/v1/movies/<int:movie_id>/` 

#### 영화 상세 가져오기
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | GET | 200(성공), 401(인증실패), 404(영화 찾지 못함) | True | | |

  - 리턴 데이터 타입
    ```js
    [
      {
        id: Number,
        title: String,  // 한글 타이틀
        sub_title: String,  // 영어 타이틀
        poster: String,
        rating: Float,
        pub_date: 'YYYY-MM-DD',
        runtime: Number,
        overview: String,
        audits: String, // 12세 관람가, 15세 관람가 등
        audi_cnt: Number, // 관객수
        genres: [
          {
            id: Number,
            name: String,
          },
          // ...
        ],
        actors: [
          {
            id: Number,
            name: String,
          },
          // ...
        ],
        directors: [
          {
            id: Number,
            name: String,
          },
          // ...
        ],
        nations: [
          {
            id: Number,
            name: String,
          },
          // ...
        ],
      },
      // ...
    ]
    ```


<br />

### `/api/v1/movies/<int:movie_id>/reviews/`

#### 영화에 대한 리뷰 모두 가져오기
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | GET | 200(성공), 401(인증실패), 404(영화 찾지 못함) | True | | |

  - 리턴 데이터 타입
    ```js
    [
      {
        id: Number,
        rating: Float,
        content: String,
        creator: {
          id: Number,
          username: String,
        },
        movie: {
          id: Number,
          title: String,
          poster: String,
        },
        formatted_time: 'YYYY-MM-DD',
        likes_count: Number,
        unlikes_count: Number,
        is_liked: Boolean,
        is_unliked: Boolean,
      },
      // ...
    ]
    ```

#### 영화에 대한 리뷰 게시
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | POST | 201(성공), 400(요청 데이터 오류), 401(인증실패), 404(영화 찾지 못함) | True | rating(float)(필수), content(string)(필수) |  |

  - 리턴 데이터 타입
    ```js
    {
      id: Number,
      rating: Float,
      content: String,
      creator: {
        id: Number,
        username: String,
      },
      movie: {
        id: Number,
        title: String,
        poster: String,
      },
      formatted_time: 'YYYY-MM-DD',
      likes_count: Number,
      unlikes_count: Number,
      is_liked: Boolean,
      is_unliked: Boolean,
    }
    ```

<br />

### `/api/v1/movies/reviews/<int:review_id>/`

#### 리뷰 수정
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | PUT | 200(성공), 400(요청 데이터 오류), 401(인증실패), 404(영화 찾지 못함) | True | rating(float)(필수), content(string)(필수) |  |

  - 리턴 데이터 타입
    ```js
    {
      id: Number,
      rating: Float,
      content: String,
      creator: {
        id: Number,
        username: String,
      },
      movie: {
        id: Number,
        title: String,
        poster: String,
      },
      formatted_time: 'YYYY-MM-DD',
      likes_count: Number,
      unlikes_count: Number,
      is_liked: Boolean,
      is_unliked: Boolean,
    }
    ```

#### 리뷰 삭제
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | DELETE | 204(성공), 401(인증실패), 404(영화 찾지 못함) | True | |  |



<br />

### `/api/v1/movies/reviews/<int:review_id>/like/`

#### 리뷰 좋아요 / 좋아요 취소
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | GET | 201(좋아요), 204(좋아요 취소), 401(인증실패), 404(영화 찾지 못함) | True |  |  |


<br />

### `/api/v1/movies/reviews/<int:review_id>/unlike/`

#### 리뷰 싫어요 / 싫어요 취소
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | GET | 201(싫어요), 204(싫어요 취소), 401(인증실패), 404(영화 찾지 못함) | True |  |  |
