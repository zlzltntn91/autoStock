import pandas as pd
import time as t
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

df = pd.DataFrame()

# 분당 시세
timeSiseUrl = 'https://finance.naver.com/item/sise_time.nhn?code={}&thistime={}&page={}'

# 삼성전자
code = "005930"

# import time
time = t.strftime("%Y%m%d%H%M%S", t.localtime())

# 첫페이지 URL
firstPageNum = 1
timeSiseFullUrl = timeSiseUrl.format(code, time, firstPageNum)
print(timeSiseFullUrl)
# 마지막 페이지 수 얻기
with urlopen(timeSiseFullUrl) as doc:
    html = bs(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')
    # print(pgrr.prettify())
    url = pgrr.a['href']
    lastPage: str = url[url.find("page=") + 5:]  # FIXME 더 좋은 방법?

print("마지막 페이지 : ", lastPage)

# 첫페이지부터 마지막페이지까지 조회 결과를 DataFrame으로
for i in range(firstPageNum, int(lastPage)):
    df = df.append(pd.read_html(timeSiseUrl.format(code, time, i), header=0)[0])

df = df.dropna()

t = df[(df['체결시각'] > '15:30')]
macketEnd = int(t['변동량'].sum())

# print(df.head(30))
print(df[(df['체결가'] >= df['체결가'].max())].head(10))
print("고가 : ", df['체결가'].max())
print("저가 : ", df['체결가'].min())
# print('장 종료후 거래량 : ', macketEnd)
