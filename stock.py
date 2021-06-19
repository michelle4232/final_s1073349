from datetime import timedelta, datetime

#ref: http://twstock.readthedocs.io/zh_TW/latest/quickstart.html#id2
import twstock

import matplotlib

def stocksFind(text):
    matplotlib.use('Agg') # ref: https://matplotlib.org/faq/howto_faq.html
    content = ''

    stock_rt = twstock.realtime.get(text)
    my_datetime = datetime.fromtimestamp(stock_rt['timestamp'] + 8 * 60 * 60)
    my_time = my_datetime.strftime('%H:%M:%S')

    content += '%s (%s) %s\n' % (
        stock_rt['info']['name'],
        stock_rt['info']['code'],
        my_time)
    content += '現價: %s / 開盤: %s\n' % (
        stock_rt['realtime']['latest_trade_price'],
        stock_rt['realtime']['open'])
    content += '最高: %s / 最低: %s\n' % (
        stock_rt['realtime']['high'],
        stock_rt['realtime']['low'])
    content += '量: %s\n' % (stock_rt['realtime']['accumulate_trade_volume'])

    stock = twstock.Stock(text)  # twstock.Stock('2330')
    content += '-----\n'
    content += '最近五日價格: \n'
    price5 = stock.price[-5:][::-1]
    date5 = stock.date[-5:][::-1]
    for i in range(len(price5)):
        # content += '[%s] %s\n' %(date5[i].strftime("%Y-%m-%d %H:%M:%S"), price5[i])
        content += '[%s] %s\n' % (date5[i].strftime("%Y-%m-%d"), price5[i])

    return content

#a = stocksFind()
#print(a)