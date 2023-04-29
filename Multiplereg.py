import pandas
from sklearn import linear_model

#  csv va excel fayllaridagi ma'lumotlarni o`qish u-n
df = pandas.read_csv("data.csv")


X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)
#  regr obyektida  erkin va erkin bo`lmagan  qiymat parametrlarini oladigan
#  bog`liqlikni e`lon qiladigan data bilan regressiya
#  obyektini to`ldiradigan fit() metodi mavjud

# predict the CO2 emission of a car where
# the weight is 2300kg, and the volume is 1300cm3:
predicted_CO2 = regr.predict([[2400, 1300]])

print("predict qilinadigan CO2 ning qiymati: ",predicted_CO2)
print(regr.coef_)



