## User API

     
### `/rest-auth/registration/` ( 회원가입 )
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  |POST | 201(성공), 400(실패) | False | username(필수), password1(필수), password2(필수) | |
  - 요청 데이터 예시
    ```js
    {
      username: 'testuser',
      password1: 'testpassword',
      password2: 'testpassword',
    }
    ```
  - 리턴 데이터 타입
    ```js
    {
      token: String,
      user: {
        id: Number,
        username: String,
      }
    }
    ```

<br />

### `/rest-auth/login/` ( 로그인 )
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  |POST | 200(성공), 401(인증 실패) | False | username(필수), password(필수) | |
  - 요청 데이터 예시
    ```js
    {
      username: 'testuser',
      password: 'testpassword',
    }
    ```
  - 리턴 데이터 타입
    ```js
    {
      token: String,
      user: {
        id: Number,
        username: String,
      }
    }
    ```

<br />

### `/rest-auth/logout/` ( 로그아웃 )
  | 메서드 | 상태 코드 | 인증 필요 여부 | 필수 요청 데이터 | query string |
  | --- | --- | --- | --- | --- |
  | GET | 200(성공), 400(실패) | True |  |  |
