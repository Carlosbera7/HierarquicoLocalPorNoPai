# HierarquicoLocalPorNoPai
'''
PS T:\ProjetoPython\Grafo> & C:/Users/CARLOS.SILVA/AppData/Local/Programs/Python/Python311/python.exe t:/ProjetoPython/Grafo/valido/c.py
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\CARLOS.SILVA\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
2025-07-14 10:43:35,164 - INFO - Carregando os dados...
2025-07-14 10:43:36,915 - INFO - ✅ Rótulos mantidos após filtragem: ['Hate.speech', 'Sexism', 'Body', 'Racism', 'Ideology', 'Homophobia', 'Origin',
 'Religion', 'OtherLifestyle', 'Fat.people', 'Left.wing.ideology', 'Ugly.people', 'Black.people', 'Fat.women', 'Feminists', 'Gays', 'Immigrants', 'Islamists', 'Lesbians', 'Men', 'Muslims', 'Refugees', 'Trans.women', 'Women', 'Transexuals', 'Ugly.women', 'Migrants', 'Homossexuals']
2025-07-14 10:43:37,237 - INFO - 📐 Partições: X_train: (3967, 5000), y_train: (3967, 28), X_test: (1701, 5000), y_test: (1701, 28)
2025-07-14 10:43:37,237 - INFO - 
🔷 [Nó] Sexism - Treinando com 470 positivos, 3497 negativos
2025-07-14 10:43:37,623 - INFO - 
📊 Relatório para 'Sexism':
              precision    recall  f1-score   support

           0       0.92      0.96      0.94      1499
           1       0.56      0.37      0.44       202

    accuracy                           0.89      1701
   macro avg       0.74      0.66      0.69      1701
weighted avg       0.88      0.89      0.88      1701

2025-07-14 10:43:37,964 - INFO -   🔹 [Subnó] Women - Avaliando 131 exemplos condicionados
2025-07-14 10:43:37,973 - INFO - 📊 Relatório para 'Women':
              precision    recall  f1-score   support

           0       0.86      0.51      0.64        74
           1       0.59      0.89      0.71        57

    accuracy                           0.68       131
   macro avg       0.72      0.70      0.68       131
weighted avg       0.74      0.68      0.67       131

2025-07-14 10:43:38,296 - INFO -   🔹 [Subnó] Men - Avaliando 131 exemplos condicionados
2025-07-14 10:43:38,305 - INFO - 📊 Relatório para 'Men':
              precision    recall  f1-score   support

           0       0.97      0.97      0.97       120
           1       0.70      0.64      0.67        11

    accuracy                           0.95       131
   macro avg       0.83      0.81      0.82       131
weighted avg       0.94      0.95      0.95       131

2025-07-14 10:43:38,555 - INFO -   🔹 [Subnó] Trans.women - Avaliando 131 exemplos condicionados
2025-07-14 10:43:38,564 - INFO - 📊 Relatório para 'Trans.women':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00       131

    accuracy                           1.00       131
   macro avg       1.00      1.00      1.00       131
weighted avg       1.00      1.00      1.00       131

2025-07-14 10:43:38,853 - INFO -   🔹 [Subnó] Feminists - Avaliando 131 exemplos condicionados
2025-07-14 10:43:38,862 - INFO - 📊 Relatório para 'Feminists':
              precision    recall  f1-score   support

           0       0.97      0.94      0.96       124
           1       0.30      0.43      0.35         7

    accuracy                           0.92       131
   macro avg       0.63      0.69      0.65       131
weighted avg       0.93      0.92      0.92       131

2025-07-14 10:43:39,152 - INFO -   🔹 [Subnó] Fat.women - Avaliando 131 exemplos condicionados
2025-07-14 10:43:39,160 - INFO - 📊 Relatório para 'Fat.women':
              precision    recall  f1-score   support

           0       0.99      0.92      0.95       108
           1       0.71      0.96      0.81        23

    accuracy                           0.92       131
   macro avg       0.85      0.94      0.88       131
weighted avg       0.94      0.92      0.93       131

2025-07-14 10:43:39,344 - INFO -   🔹 [Subnó] Transexuals - Avaliando 131 exemplos condicionados
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
2025-07-14 10:43:39,355 - INFO - 📊 Relatório para 'Transexuals':
              precision    recall  f1-score   support

           0       0.99      1.00      1.00       130
           1       0.00      0.00      0.00         1

    accuracy                           0.99       131
   macro avg       0.50      0.50      0.50       131
weighted avg       0.98      0.99      0.99       131

2025-07-14 10:43:39,680 - INFO -   🔹 [Subnó] Ugly.women - Avaliando 131 exemplos condicionados
2025-07-14 10:43:39,689 - INFO - 📊 Relatório para 'Ugly.women':
              precision    recall  f1-score   support

           0       0.97      0.96      0.96       112
           1       0.76      0.84      0.80        19

    accuracy                           0.94       131
   macro avg       0.87      0.90      0.88       131
weighted avg       0.94      0.94      0.94       131

2025-07-14 10:43:39,689 - INFO -
🔷 [Nó] Body - Treinando com 126 positivos, 3841 negativos
2025-07-14 10:43:39,997 - INFO - 
📊 Relatório para 'Body':
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      1663
           1       0.84      0.68      0.75        38

    accuracy                           0.99      1701
   macro avg       0.92      0.84      0.87      1701
weighted avg       0.99      0.99      0.99      1701

2025-07-14 10:43:40,285 - INFO -   🔹 [Subnó] Fat.people - Avaliando 31 exemplos condicionados
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
2025-07-14 10:43:40,295 - INFO - 📊 Relatório para 'Fat.people':
              precision    recall  f1-score   support

           0       0.00      0.00      0.00         7
           1       0.77      1.00      0.87        24

    accuracy                           0.77        31
   macro avg       0.39      0.50      0.44        31
weighted avg       0.60      0.77      0.68        31

2025-07-14 10:43:40,602 - INFO -   🔹 [Subnó] Fat.women - Avaliando 31 exemplos condicionados
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
2025-07-14 10:43:40,611 - INFO - 📊 Relatório para 'Fat.women':
              precision    recall  f1-score   support

           0       0.00      0.00      0.00         9
           1       0.71      1.00      0.83        22

    accuracy                           0.71        31
   macro avg       0.35      0.50      0.42        31
weighted avg       0.50      0.71      0.59        31

2025-07-14 10:43:40,918 - INFO -   🔹 [Subnó] Ugly.people - Avaliando 31 exemplos condicionados
2025-07-14 10:43:40,926 - INFO - 📊 Relatório para 'Ugly.people':
              precision    recall  f1-score   support

           0       0.80      0.67      0.73        12
           1       0.81      0.89      0.85        19

    accuracy                           0.81        31
   macro avg       0.80      0.78      0.79        31
weighted avg       0.81      0.81      0.80        31

2025-07-14 10:43:41,233 - INFO -   🔹 [Subnó] Ugly.women - Avaliando 31 exemplos condicionados
2025-07-14 10:43:41,242 - INFO - 📊 Relatório para 'Ugly.women':
              precision    recall  f1-score   support

           0       0.80      0.62      0.70        13
           1       0.76      0.89      0.82        18

    accuracy                           0.77        31
   macro avg       0.78      0.75      0.76        31
weighted avg       0.78      0.77      0.77        31

2025-07-14 10:43:41,243 - INFO -
🔷 [Nó] Racism - Treinando com 66 positivos, 3901 negativos
2025-07-14 10:43:41,560 - INFO - 
📊 Relatório para 'Racism':
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      1673
           1       0.50      0.04      0.07        28

    accuracy                           0.98      1701
   macro avg       0.74      0.52      0.53      1701
weighted avg       0.98      0.98      0.98      1701

2025-07-14 10:43:41,822 - INFO -   🔹 [Subnó] Black.people - Avaliando 2 exemplos condicionados
2025-07-14 10:43:41,830 - INFO - 📊 Relatório para 'Black.people':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         1
           1       1.00      1.00      1.00         1

    accuracy                           1.00         2
   macro avg       1.00      1.00      1.00         2
weighted avg       1.00      1.00      1.00         2

2025-07-14 10:43:41,831 - INFO -
🔷 [Nó] Ideology - Treinando com 64 positivos, 3903 negativos
2025-07-14 10:43:42,144 - INFO - 
📊 Relatório para 'Ideology':
              precision    recall  f1-score   support

           0       0.99      0.99      0.99      1673
           1       0.17      0.11      0.13        28

    accuracy                           0.98      1701
   macro avg       0.58      0.55      0.56      1701
weighted avg       0.97      0.98      0.97      1701

2025-07-14 10:43:42,344 - INFO -   🔹 [Subnó] Left.wing.ideology - Avaliando 18 exemplos condicionados
2025-07-14 10:43:42,354 - INFO - 📊 Relatório para 'Left.wing.ideology':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        18

    accuracy                           1.00        18
   macro avg       1.00      1.00      1.00        18
weighted avg       1.00      1.00      1.00        18

2025-07-14 10:43:42,655 - INFO -   🔹 [Subnó] Feminists - Avaliando 18 exemplos condicionados
2025-07-14 10:43:42,663 - INFO - 📊 Relatório para 'Feminists':
              precision    recall  f1-score   support

           0       0.67      0.13      0.22        15
           1       0.13      0.67      0.22         3

    accuracy                           0.22        18
   macro avg       0.40      0.40      0.22        18
weighted avg       0.58      0.22      0.22        18

2025-07-14 10:43:42,668 - INFO -
🔷 [Nó] Homophobia - Treinando com 225 positivos, 3742 negativos
2025-07-14 10:43:42,989 - INFO - 
📊 Relatório para 'Homophobia':
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      1604
           1       0.95      0.63      0.76        97

    accuracy                           0.98      1701
   macro avg       0.97      0.81      0.87      1701
weighted avg       0.98      0.98      0.97      1701

2025-07-14 10:43:43,227 - INFO -   🔹 [Subnó] Gays - Avaliando 64 exemplos condicionados
2025-07-14 10:43:43,234 - INFO - 📊 Relatório para 'Gays':
              precision    recall  f1-score   support

           0       0.97      1.00      0.98        60
           1       1.00      0.50      0.67         4

    accuracy                           0.97        64
   macro avg       0.98      0.75      0.83        64
weighted avg       0.97      0.97      0.96        64

2025-07-14 10:43:43,529 - INFO -   🔹 [Subnó] Homossexuals - Avaliando 64 exemplos condicionados
2025-07-14 10:43:43,536 - INFO - 📊 Relatório para 'Homossexuals':
              precision    recall  f1-score   support

           0       1.00      0.71      0.83         7
           1       0.97      1.00      0.98        57

    accuracy                           0.97        64
   macro avg       0.98      0.86      0.91        64
weighted avg       0.97      0.97      0.97        64

2025-07-14 10:43:43,794 - INFO -   🔹 [Subnó] Lesbians - Avaliando 64 exemplos condicionados
2025-07-14 10:43:43,803 - INFO - 📊 Relatório para 'Lesbians':
              precision    recall  f1-score   support

           0       1.00      0.71      0.83         7
           1       0.97      1.00      0.98        57

    accuracy                           0.97        64
   macro avg       0.98      0.86      0.91        64
weighted avg       0.97      0.97      0.97        64

2025-07-14 10:43:43,803 - INFO -
🔷 [Nó] Origin - Treinando com 18 positivos, 3949 negativos
2025-07-14 10:43:44,065 - INFO - 
📊 Relatório para 'Origin':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      1693
           1       0.00      0.00      0.00         8

    accuracy                           0.99      1701
   macro avg       0.50      0.50      0.50      1701
weighted avg       0.99      0.99      0.99      1701

2025-07-14 10:43:44,066 - INFO - 
🔷 [Nó] Religion - Treinando com 21 positivos, 3946 negativos
2025-07-14 10:43:44,329 - INFO - 
📊 Relatório para 'Religion':
              precision    recall  f1-score   support

           0       0.99      1.00      1.00      1692
           1       0.00      0.00      0.00         9

    accuracy                           0.99      1701
   macro avg       0.50      0.50      0.50      1701
weighted avg       0.99      0.99      0.99      1701

2025-07-14 10:43:44,497 - INFO -   🔹 [Subnó] Islamists - Avaliando 4 exemplos condicionados
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Recall is ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Recall is ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Recall is ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
2025-07-14 10:43:44,507 - INFO - 📊 Relatório para 'Islamists':
              precision    recall  f1-score   support

           0       1.00      0.25      0.40         4
           1       0.00      0.00      0.00         0

    accuracy                           0.25         4
   macro avg       0.50      0.12      0.20         4
weighted avg       1.00      0.25      0.40         4

2025-07-14 10:43:44,659 - INFO -   🔹 [Subnó] Muslims - Avaliando 4 exemplos condicionados
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Recall is ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Recall is ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
C:\Users\CARLOS.SILVA\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\metrics\_classification.py:1565: UndefinedMetricWarning: Recall is ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", len(result))
2025-07-14 10:43:44,668 - INFO - 📊 Relatório para 'Muslims':
              precision    recall  f1-score   support

           0       1.00      0.75      0.86         4
           1       0.00      0.00      0.00         0

    accuracy                           0.75         4
   macro avg       0.50      0.38      0.43         4
weighted avg       1.00      0.75      0.86         4

2025-07-14 10:43:44,669 - INFO - 
🔷 [Nó] Migrants - Treinando com 57 positivos, 3910 negativos
2025-07-14 10:43:44,997 - INFO - 
📊 Relatório para 'Migrants':
              precision    recall  f1-score   support

           0       0.99      0.99      0.99      1676
           1       0.32      0.24      0.27        25

    accuracy                           0.98      1701
   macro avg       0.65      0.62      0.63      1701
weighted avg       0.98      0.98      0.98      1701

2025-07-14 10:43:45,122 - INFO -   🔹 [Subnó] Immigrants - Avaliando 19 exemplos condicionados
2025-07-14 10:43:45,131 - INFO - 📊 Relatório para 'Immigrants':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        19

    accuracy                           1.00        19
   macro avg       1.00      1.00      1.00        19
weighted avg       1.00      1.00      1.00        19

2025-07-14 10:43:45,445 - INFO -   🔹 [Subnó] Refugees - Avaliando 19 exemplos condicionados
2025-07-14 10:43:45,454 - INFO - 📊 Relatório para 'Refugees':
              precision    recall  f1-score   support

           0       1.00      0.08      0.14        13
           1       0.33      1.00      0.50         6

    accuracy                           0.37        19
   macro avg       0.67      0.54      0.32        19
weighted avg       0.79      0.37      0.26        19

2025-07-14 10:43:45,455 - INFO -
           0       1.00      1.00      1.00      1695
           1       0.60      0.50      0.55         6

    accuracy                           1.00      1701
   macro avg       0.80      0.75      0.77      1701
weighted avg       1.00      1.00      1.00      1701
'''
