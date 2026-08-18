import pandas as pd
import numpy as np

def generate(n=200):
    years = list(range(2000, 2000+n))
    pop = (np.linspace(1_000_000, 2_000_000, n) + np.random.normal(0,20000,n)).astype(int)
    urban = (50 + np.random.normal(0,5,n)).round(1)
    df = pd.DataFrame({'year':years,'population':pop,'urban_pct':urban})
    df.to_csv('data/population_large.csv', index=False)
    print('Wrote data/population_large.csv')

if __name__=='__main__':
    generate(120)
