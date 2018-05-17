import requests
import pandas as pd

url = 'https://api.census.gov/data/2016/acs/acs5/profile'
# DP02_0064PE is EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor's degree
# DP05_0032PE is RACE!!One race!!White
# DP03_0096PE is Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage
params = {'get':'DP02_0064PE,DP05_0032PE,DP03_0096PE,NAME',
          'for':'county:*',
          'in':'state:51'}
j = requests.get(url, params=params).json()
df = pd.DataFrame(j[1:], columns=j[0])
df.columns = ['P_COLLEGE', 'P_WHITE', 'P_INSURED', 'NAME', 'state', 'county']
df.to_csv('acs.csv', index=False)
