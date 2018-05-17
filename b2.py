import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('republican_shares.csv')
df.set_index(['County', 'Year'], inplace=True)

df = df['Republican Share'].unstack(level='County')
df[['Accomack County', 'Amelia County', 'Amherst County', 'Alleghany County']].plot()
plt.savefig('republican_share.png')
