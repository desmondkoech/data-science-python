# pip install pandas matplotlib scikit-learn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data/population.csv')
plt.plot(df['year'], df['population'], marker='o')
plt.title('Population over time')
plt.xlabel('Year')
plt.ylabel('Population')
plt.tight_layout()
plt.savefig('outputs/population_plot.png')

# quick regression predict population
X = df[['year']]
y = df['population']
model = LinearRegression().fit(X,y)
pred = model.predict([[2020]])
with open('outputs/model_prediction.txt','w') as f:
    f.write(f'coef={model.coef_[0]:.2f}, intercept={model.intercept_:.2f}, pred2020={pred[0]:.0f}')
print('Done: outputs written to outputs/')
