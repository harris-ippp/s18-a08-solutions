import requests
import pandas as pd

election_ids = pd.read_csv('election_ids.csv')
prefix = 'http://historical.elections.virginia.gov/elections/download/'
suffix='/precincts_include:0/'

for i,row in election_ids.iterrows():
    year = row['year']
    election_id = row['election_id']
    print(year)

    response = requests.get(prefix + str(election_id) + suffix)
    with open('data/' + str(year) + '.csv', 'w') as f:
        f.write(response.text)
