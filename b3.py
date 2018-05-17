import requests
import pandas as pd

url = 'https://api.census.gov/data/2016/acs/acs5/profile'
# DP02_0064PE is EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor's degree
# DP05_0032PE is RACE!!One race!!White
# DP03_0062E is Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!Median household income (dollars)
params = {'get':'DP02_0064PE,DP05_0032PE,DP03_0062E,NAME',
          'for':'county:*',
          'in':'state:51'}
j = requests.get(url, params=params).json()
df = pd.DataFrame(j[1:], columns=j[0])
df.columns = ['P_COLLEGE', 'P_WHITE', 'MEDIAN_INCOME', 'NAME', 'state', 'county']
df.to_csv('acs.csv', index=False)
