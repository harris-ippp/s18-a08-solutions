import requests
from bs4 import BeautifulSoup
import pandas as pd

base = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'
response = requests.get(base)
page = BeautifulSoup(response.text, 'html.parser')

prefix = 'http://historical.elections.virginia.gov/elections/download/'
suffix = '/precincts_include:0/'


election_items = page.find_all('tr', class_='election_item general_party')

years = []
election_ids = []

for i in election_items:
    election_ids.append(i.attrs['id'][12:])
    years.append(i.find(class_='year').text)

df = pd.DataFrame({'year':years, 'election_id':election_ids})
df.to_csv('election_ids.csv', index=False)
