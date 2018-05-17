import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

share = pd.read_csv('republican_shares.csv')
acs = pd.read_csv('acs.csv')

share = share[share.Year == 2016]
share['County/City'] = share['County/City'].str.upper()
acs['County/City'] = acs['NAME'].str[:-10].str.upper()

df = share.merge(acs, on='County/City')

sns.pairplot(df, vars=['P_COLLEGE', 'P_WHITE', 'P_INSURED', 'R_SHARE'])
plt.savefig('pairplot.png')

res = smf.ols('R_SHARE ~ P_COLLEGE + P_WHITE + P_INSURED', df).fit()
print(res.summary())
