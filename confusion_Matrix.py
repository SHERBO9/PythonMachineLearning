# Confusion matrix (Chalkashlik matritsasi) -Bu modeldagi xatolarga yo'l qo'yilganligini
# baholash uchun klassifikatsiya muammolarida ishlatiladigan jadval.


import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix,
                                            display_labels=[False, True])
#  Accuracy- aniqlikni hisoblash: (True Positive + True Negative) / Total Predictions
Accuracy = metrics.accuracy_score(actual, predicted)

# Precision - predict qilingan positivlarning necha % haqiqiy positivligi
# (True Positive / (True Positive + False Positive))
Precision = metrics.precision_score(actual, predicted)

# Sensitivity (Recall) -   Barcha predict qilingan positiv
# holatlarning necha % positiv predict qilinganligi (True Positive / (True Positive + False Positive))
Sensitivity_recall = metrics.recall_score(actual, predicted)

# Specificity - Model salbiy natijalarni bashorat qilishda qanchalik yaxshiligi
# True Negative / (True Negative + False Positive)
Specificity = metrics.recall_score(actual, predicted, pos_label=0)

# F-score   - F-ball  aniqlik va sezgirlikning "Garmonik o'rtachasi" dir.
# 2 * ((Precision * Sensitivity) / (Precision + Sensitivity))
F1_score = metrics.f1_score(actual, predicted)

#  Hisoblashlar
print({"Accuracy": Accuracy, "Precision": Precision,
       "Sensitivity_recall": Sensitivity_recall,
       "Specificity": Specificity,
       "F1_score": F1_score})
# Grafikni tasvirlash
cm_display.plot()
plt.show()
