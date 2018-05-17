import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('republican_shares.csv')
df.set_index(['County/City', 'Year'], inplace=True)

df = df['R_SHARE'].unstack(level='County/City')
ax = df[['Accomack County', 'Amelia County', 'Amherst County', 'Alleghany County']].plot()

ax.set_title('Virginia Republican Presidential Vote Share', fontsize=20)
ax.set_ylabel('Republican Vote Share')
plt.savefig('republican_shares.png')
