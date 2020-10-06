import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import time

url = 'https://finance.naver.com/item/sise_day.nhn?code={}&page={}'
code = '005930'
firstPage = 1
firstPageFullUrl = url.format(code, firstPage)

# 마지막 페이지 구하기
with urlopen(firstPageFullUrl) as doc:
    html = bs(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')
    # print(type(pgrr)) # <class 'bs4.element.Tag'>
    # print(pgrr.prettify())
    hrefUrl: str = pgrr.a['href']
    lastPageNum = hrefUrl[hrefUrl.find('page=') + 5:]

# 성능체크
now = time.time()
df = pd.DataFrame()
for i in range(firstPage, int(lastPageNum)):
    df = df.append(pd.read_html(url.format(code, i), header=0)[0])
    if i == 1:
        df = df.dropna()
        print(f'시가 : {df["시가"][0:1].values[0]}')
        print(f'고가 : {df["고가"][0:1].values[0]}')
        print(f'저가 : {df["저가"][0:1].values[0]}')
        print(f'종가 : {df["종가"][0:1].values[0]}')

print(f'performance : {int(time.time() - now)}')
df = df.dropna()
# print(df)

from matplotlib import pyplot as plt
from matplotlib import dates as mdates
# from mpl_finance import candlestick_ohlc # warning
from mplfinance.original_flavor import candlestick_ohlc
from datetime import datetime

df = df.sort_values(by='날짜')
for i in range(0, len(df)):
    dt = datetime.strftime(df['날짜'].values[i], '%Y.%m.%d').date()
    print(str(dt))
    df['날짜'].values[i] = mdates.date2num(dt)

ohlc = df[['날짜', '시가', '고가', '저가', '종가']]
