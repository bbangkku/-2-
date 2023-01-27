import requests
from pprint import pprint


def credits(title):
# 영화검색 받아오기
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'  
    params = {
        'api_key' : '751ffb7fa6d11ea4857ba676f9ca71be',
        'language' : 'ko',
        'region' : 'KR',
        'query' : title,
        'include_adult' : 'false'
    }
# 출연진 받아오기
    response = requests.get(BASE_URL + path, params=params).json()
    xx = response['results']
# 값이 없으면 None 반환
    if len(xx) == 0:
        return None
# 값이 있으면 출연진 반환
    path2 = "/movie/{}/credits".format(response['results'][0]['id'])
    params2 = {
        'api_key' : '751ffb7fa6d11ea4857ba676f9ca71be', 
        'language' : 'ko',
        'region' : 'KR',  
    }

    response2 = requests.get(BASE_URL + path2, params=params2).json()
    d = {}
    
    cast_li = []
    crew_li = []
    for i in range(len(response2['cast'])):
        if response2['cast'][i]['cast_id'] < 10:
            cast_li.append(response2['cast'][i]['name'])
    for i in range(len(response2['crew'])):
        if response2['crew'][i]['department'] == 'Directing':
            crew_li.append(response2['crew'][i]['name'])
    d['cast'] = cast_li
    d['directing'] = crew_li
    return d

     
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
