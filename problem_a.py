import requests


def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'  
    params = {
        'api_key' : '751ffb7fa6d11ea4857ba676f9ca71be',
        'language' : 'ko',
        'region' : 'KR'
    }
    # 요청 및 응답
    response = requests.get(BASE_URL + path, params=params).json()

    # 결과 ( 영화 정보들은 'results' 키로 조회 가능)
    return len(response.get('results'))
    # 
   
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
