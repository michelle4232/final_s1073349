# 目標位置>>Yahoo>>電影>>Yahoo即將上映
# https://tw.movies.yahoo.com/movie_thisweek.html

import requests
from bs4 import BeautifulSoup


def check_req_url(url):  # 測試請求網址是否請求成功
    resp = requests.get(url)  # 請求網址
    # print(resp.status_code) #錯誤時404,成功時200
    if resp.status_code != 200:  # 如果請求失敗
        print('Invalid url:', resp.url)  # 印出請求失敗的網址
        return "fail"  # 回傳失敗提示訊息
    else:
        return resp.text  # 回傳請求成功的html文字


def get_week_new_movies(webpage):  # 抓取電影資訊
    soup = BeautifulSoup(webpage, 'html.parser')  # 網頁解析
    movies = []  # 域設電影資訊存這裡

    # 抓取<div class="release_info_text"></div>內文字
    rows = soup.find_all('div', 'release_info_text')
    data_movie = dict()
    # print(rows)
    for row in rows:
        data_movie = dict()  # 存成{"key":"value"}格式
        # 電影名稱
        data_movie['ch_name'] = row.find('div', 'release_movie_name').a.text.strip()
        # 英文名稱
        data_movie['english_name'] = row.find('div', 'release_movie_name').find('div', 'en').a.text.strip()
        movies.append(data_movie)  # 再被取代前先存入for 外面的movies=[]

    text = ''
    for movie in movies:
        name = str(movie['ch_name'])
        en_name = str(movie['english_name'])
        #print(movie['ch_name'])
        text += (name + '(' + en_name + ')' + '\n')
    #print(text)

    return text



#get_week_new_movies(webpage)
