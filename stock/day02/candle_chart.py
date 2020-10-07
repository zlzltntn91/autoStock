import mplfinance as mpf
import pandas as pd

from stock.day01.day_sise import DaySise

ds = DaySise()
last_page = ds.get_last_page('005930')
df = pd.DataFrame()

df = ds.get_data_frame('005930', 10)
df = df.iloc[0:30]
df = df.rename(columns={'날짜': 'Date',
                        '시가': 'Open',
                        '고가': 'High',
                        '저가': 'Low',
                        '종가': 'Close',
                        '거래량': 'Volume'})
df = df.sort_values(by='Date')
df.index = pd.to_datetime(df.Date)
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

# mpf.plot(df, title='Samsung candle chart', type='ohlc')
mpf.plot(df, title='Samsung candle chart', type='candle')
