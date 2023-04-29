import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# berilgan data    x-> kunning vaqtlari
# y-> shu vaqtdagi trassadagi mashina tezliklari
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15,
     16, 18, 19, 21, 22]
y = [100, 90, 20, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90,
     99, 99, 100]

# NumPy ning polynomial modelini qurish metodi
#  7-darajali funksiya
plynm_model = numpy.poly1d(numpy.polyfit(x, y, 3))

#  data pointlar orasini 1 dan 22 gacha 100 bo`lakka bo`ladi
plymn_line = numpy.linspace(1, 22, 100)

# data point larni tasvirlash
plt.scatter(x, y)

#  Berilgan data pointlardan chiziqni chizish
plt.plot(plymn_line, plynm_model(plymn_line))
plt.show()

#  R-squared   Bog`liqlikni topish:

print(r2_score(y, plynm_model(x)))

speed = plynm_model(15.5)
print("15:30 dagi tezlik: ", speed)
