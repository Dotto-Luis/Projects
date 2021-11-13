from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://coinmarketcap.com/currencies/ripple/historical-data/?start=20130428&end=20180802"
content = requests.get(url).content
soup = BeautifulSoup(content,'html.parser')
table = soup.find('table', {'class': 'table'})

data = [[td.text.strip() for td in tr.findChildren('td')]
        for tr in table.findChildren('tr')]

df = pd.DataFrame(data)
df.drop(df.index[0], inplace=True) # first row is empty
df[0] =  pd.to_datetime(df[0]) # date
for i in range(1,7):
    df[i] = pd.to_numeric(df[i].str.replace(",","").str.replace("-","")) # some vol is missing and has -
df.columns = ['Date','Open','High','Low','Close','Volume','Market Cap']
df.set_index('Date',inplace=True)
df.sort_index(inplace=True)

