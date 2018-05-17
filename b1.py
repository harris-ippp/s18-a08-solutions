import pandas as pd

def to_number(series):
    """
    Given a series containing numbers represented as strings with commas
    Return a series of integers
    """
    return series.str.replace(',','').astype(int)

def get_county(county_city):
    """
    Given a county name that may also contains a congressional district
    Return just the county name
    """
    paren = county_city.find('(')
    if paren == -1:
        return county_city
    else:
        return county_city[:paren-1]


elections = pd.read_csv('election_ids.csv')
dfs = []

for i,row in elections.iterrows():
    year = row['year']
    df = pd.read_csv('data/' + str(year) + '.csv')

    parties = df.loc[0]
    df.drop(0, inplace=True)
    republican_column = parties[parties == 'Republican'].index[0]

    df['Total Votes Cast'] = to_number(df['Total Votes Cast'])
    df[republican_column] = to_number(df[republican_column])

    df['County/City'] = df['County/City'].apply(get_county)

    df_county = df[['Total Votes Cast', republican_column]].groupby(df['County/City']).sum()
    df_county['R_SHARE'] = (df_county[republican_column] / 
                                     df_county['Total Votes Cast'])

    df_county['Year'] = year
    dfs.append(df_county[['R_SHARE', 'Year']])

df = pd.concat(dfs)
df.to_csv('republican_shares.csv')
