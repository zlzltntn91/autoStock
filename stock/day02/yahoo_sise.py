# Data visualizaion

import pandas_datareader as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

df = pdr.get_data_yahoo('005930.KS', '2017-01-01')

plt.figure(figsize=(9, 6))
plt.subplot(2, 1, 1)
plt.title('Samsung (Yahoo)')
plt.plot(df.index, df['Close'], 'c', label='Close')
plt.plot(df.index, df['Adj Close'], 'b--', label='Adj Close')
plt.legend(loc='best')

plt.subplot(2, 1, 2)
plt.bar(df.index, df['Volume'], color='g', label='Volume')
plt.legend(loc='best')
plt.show()
