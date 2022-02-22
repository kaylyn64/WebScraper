import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml



# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/List_of_Chinese_administrative_divisions_by_population"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
chinatable=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(chinatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
print(df)

# drop the unwanted columns
data = df.drop([ "Administrative Division"], axis=1)
# rename columns for ease
data = data.rename(columns={"Administrative Division": "Province"})
print(data)