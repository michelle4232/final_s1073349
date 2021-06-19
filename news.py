import requests
from bs4 import BeautifulSoup  # 轉DOM
import pandas


def getAllComments(pageurl):
    res = requests.get(pageurl)
    soup = BeautifulSoup(res.text, 'lxml')  # 老師建議無特殊需求的話都用lxml格式讀取

    # 從list中找到每一個tit
    eachNews = soup.select('.list .tit')

    news_all = []
    #print(eachNews)
    for p in eachNews:
        url = p.get('href')
        title = p.get('title')
        time = p.select_one('.time').text

        print(time, title, url)
    return news_all


#getAllComments('https://news.ltn.com.tw/list/breakingnews')