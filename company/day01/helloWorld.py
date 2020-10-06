import pandas as pd
import time as t
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

timeSiseUrl = 'https://finance.naver.com/item/sise_time.nhn?code={}&thistime={}&page={}'

code = "005930"
time = t.strftime("%Y%m%d%H%M%S", t.localtime())

timeSiseFullUrl = timeSiseUrl.format(code, time, 1)
print(timeSiseFullUrl)
df = pd.DataFrame()

with urlopen(timeSiseFullUrl) as doc:
    html = bs(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')
    # print(pgrr.prettify())
    url = pgrr.a['href']
    lastPage: str = url[url.find("page=") + 5:]
    # print(lastPage)
