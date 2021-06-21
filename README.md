# lineBot helper

  This is a lineBot helper for myself.
  
  
## Build process

 + 測試是否可使用
   加入line好友
  * ![image](https://user-images.githubusercontent.com/62208026/122752847-06890c80-d2c4-11eb-9c5c-6084c3a0cbd2.png)
  
  * 依照功能需求在自己的line中輸入文字(輸入之訊息有固定格式)
 
 + 若要執行程式
  * 儲存檔案(直接執行main.py 即可) 
  * 需先綁定Heroku(我是用github直接連結Heroku) 
  * 將檔案拉到github中 
  * 在Heroku開啟一個專案連結github 
  * 將Heroku的url貼至使用帳號之channel的 ``Webhook URL`` 

 + 可能會出現的小問題  
  * 可能因所採用的氣象局api, 缺少某些縣市的天氣資訊 
  * linebot每個月的免費使用額度有上限50則, 因此可能無法自動回覆訊息(若有需要我測試時有錄影, 可demo影片) 
  * Heroku每個月額度也有一定的上限, 同上  


## Introduction

  由於現在大部分人皆是使用Line作為傳輸訊息之工具, 且以我來說. 我並不是一個勤勞的人, 較不愛開電腦或網頁, 因此我使用Line作為一個小幫手，幫助我達到一些我平常會想要查詢的資料。
  它包含了以下功能:
  1. 查詢天氣
  2. 翻譯
  3. 即將上映之電影
  4. 即時新聞
  5. 及時股價

## Details of the approach

## Results

+ Example
  > input: `` @天氣 新竹市 ``
  > > output: 天氣, 溫度, 降雨, 溫溼度
  > > > > <img src="https://github.com/michelle4232/final_s1073349/blob/main/photos/weather.jpg" width="300" height="600">
---------------------------------------
  > input: `` @翻譯 I am happy ``
  > > output: 我很高興
  > > > > <img src="https://github.com/michelle4232/final_s1073349/blob/main/photos/trans.jpg" width="300" height="600">
---------------------------------------
  > input:`` @電影 ``
  > > output: 最近即將上映之電影
  > > > > <img src="https://github.com/michelle4232/final_s1073349/blob/main/photos/movie.jpg" width="300" height="600">
---------------------------------------
  > input: `` @即時新聞 ``
  > > output: 最近六則新聞
  > > > > <img src="https://github.com/michelle4232/final_s1073349/blob/main/photos/news.jpg" width="300" height="600">
---------------------------------------
  > input: `` #2330 `` 
  > > output: 此股最新價格及近五日波動
  > > > > <img src="https://github.com/michelle4232/final_s1073349/blob/main/photos/stock.jpg" width="300" height="600">
---------------------------------------
## References

+ https://marketingliveincode.com/?page_id=2532
+ https://www.youtube.com/channel/UCguZS-y7codLSt6vpkVdnKg
+ https://github.com/emn178/markdown
+ https://opendata.cwb.gov.tw/dist/opendata-swagger.html
+ https://medium.com/@ethan.chen927/%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2-et-today%E6%96%B0%E8%81%9E-%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86-8d1002783c27
+ https://pypi.org/project/google-trans-new/
+ https://developers.line.biz/zh-hant/docs/messaging-api/overview/
+ https://pypi.org/project/twstock/
