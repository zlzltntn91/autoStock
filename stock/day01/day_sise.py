import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen


class DaySise:
    __URL = "https://finance.naver.com/item/sise_day.nhn?code={}"

    def get_last_page(self, code: str):
        with urlopen(self.__URL.format(code)) as doc:
            html = bs(doc, 'lxml')
            pgrr = html.find('td', class_='pgRR')
            href_url: str = pgrr.a['href']
            last_page_num: str = href_url[href_url.find('page=') + 5:]
        return last_page_num

    def get_data_frame(self, code: str, last_page: str, drop_nan: bool = True):
        df = pd.DataFrame()
        for i in range(1, int(last_page)):
            df = df.append(pd.read_html(self.__URL.format(code) + ('&page=' + str(i)), header=0)[0])
        if drop_nan is True:
            df = df.dropna()
        return df

    def get_today_ohlc(self, code: str):
        df = pd.DataFrame()
        df = df.append(pd.read_html(self.__URL.format(code) + '&page=1', header=0)[0])
        # with urlopen('https://finance.naver.com/item/main.nhn?code={}'.format(code)) as doc:
        #     html = bs(doc, 'lxml')
        #     company_name: str = html.find('div', class_='wrap_company').find('h2').a.text
        df = df.dropna()
        return {
            'code': code,
            # 'name': company_name,
            # 'day': df['날짜'].values[0],
            'value': {
                'o': int(df['시가'].values[0]),
                'h': int(df['고가'].values[0]),
                'l': int(df['저가'].values[0]),
                'c': int(df['종가'].values[0]),
                'pc': int(df['종가'].values[1])}
        }
