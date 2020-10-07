import time

from matplotlib import pyplot as plt
from stock.day01.day_sise import DaySise

ds = DaySise()
lastPageNum = ds.get_last_page('005930')

start = time.time()
df = ds.get_data_frame('005930', 2)

df = df.sort_values(by='날짜')

plt.title("Samsung Close")
plt.xticks(rotation=90)
plt.plot(df['날짜'], df['종가'], 'ro-')
plt.grid(color='gray', linestyle='--')
plt.show()
