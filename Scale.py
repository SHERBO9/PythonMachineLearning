# Scale features

# Standartlash formulasi:
# z=(x-u)/s   z-new data, x-original data,  u- mean of data, s-st. deviation

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[1500, 2.5]])

predictedCO2 = regr.predict([scaled[0]])
print("Predict qilingan CO2", predictedCO2)
