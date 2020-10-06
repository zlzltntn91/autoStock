import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

url = 'https://finance.naver.com/item/sise_day.nhn?code={}&page={}'
code = '005930'
firstPage = 1
firstPageFullUrl = url.format(code, firstPage)

with urlopen(firstPageFullUrl) as doc:
    html = bs(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')
    print(pgrr.prettify())

print(firstPageFullUrl)
