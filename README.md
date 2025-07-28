# HierarquicoLocalPorNoPai

| Nó                 | Precision (1) | Recall (1) | F1-score (1) | Accuracy total |
| ------------------ | ------------- | ---------- | ------------ | -------------- |
| Lesbians           | 0.92          | 1.00       | **0.96**     | 0.92           |
| Homossexuals       | 0.90          | 0.70       | **0.79**     | 0.91           |
| Homophobia         | 0.90          | 0.63       | **0.74**     | 0.97           |
| Ugly.people        | 0.71          | 0.77       | **0.74**     | 0.99           |
| Body               | 0.76          | 0.93       | **0.84**     | 0.95           |
| Ugly.women         | 0.76          | 0.80       | **0.78**     | 0.90           |
| Fat.women          | 0.64          | 0.91       | **0.75**     | 0.84           |
| Fat.people         | 0.71          | 0.69       | **0.70**     | 0.99           |
| Sexism             | 0.58          | 0.36       | **0.45**     | 0.89           |
| Men                | 0.75          | 0.69       | **0.72**     | 0.94           |
| OtherLifestyle     | 0.00          | 0.00       | **0.00**     | 1.00           |
| Feminists          | 0.40          | 0.67       | **0.50**     | 0.94           |
| Gays               | 0.67          | 0.50       | **0.57**     | 0.95           |
| Refugees           | 0.26          | 0.29       | **0.27**     | 0.98           |
| Migrants           | 0.25          | 0.50       | **0.33**     | 0.98           |
| Ideology           | 0.21          | 0.11       | **0.14**     | 0.98           |
| Hate.speech        | 0.68          | 0.39       | **0.49**     | 0.83           |
| Racism             | 0.40          | 0.07       | **0.12**     | 0.98           |
| Black.people       | 0.67          | 1.00       | **0.80**     | 0.80           |
| Islamists          | 0.00          | 0.00       | **0.00**     | 0.99           |
| Left.wing.ideology | 0.00          | 0.00       | **0.00**     | 0.99           |
| Immigrants         | 0.00          | 0.00       | **0.00**     | 1.00           |
| Religion           | 0.12          | 0.11       | **0.12**     | 0.98           |
| Trans.women        | 0.00          | 0.00       | **0.00**     | 0.99           |
| Transexuals        | 0.00          | 0.00       | **0.00**     | 0.99           |
| Muslims            | 0.33          | 1.00       | **0.50**     | 0.75           |
| Origin             | 0.00          | 0.00       | **0.00**     | 1.00           |
| Women              | 0.62          | 0.89       | **0.73**     | 0.70           |


# HierarquicoLocalPorNoPai
```
🔷 [Nó] Hate.speech - Treinando com 859 positivos, 3108 negativos
2025-07-24 13:54:12,936 - INFO - 
📊 Relatório para 'Hate.speech': 
              precision    recall  f1-score   support

           0       0.85      0.95      0.90      1332
           1       0.68      0.39      0.49       369

    accuracy                           0.83      1701
   macro avg       0.76      0.67      0.69      1701
weighted avg       0.81      0.83      0.81      1701

2025-07-24 13:54:13,262 - INFO -   🔹 [Subnó] Homophobia - Avaliando 211 exemplos condicionados
2025-07-24 13:54:13,272 - INFO - 📊 Relatório para 'Homophobia':
              precision    recall  f1-score   support

           0       0.99      0.96      0.98       150
           1       0.91      0.98      0.94        61

    accuracy                           0.97       211
   macro avg       0.95      0.97      0.96       211
weighted avg       0.97      0.97      0.97       211

2025-07-24 13:54:13,623 - INFO -   🔹 [Subnó] Racism - Avaliando 211 exemplos condicionados
2025-07-24 13:54:13,632 - INFO - 📊 Relatório para 'Racism':
              precision    recall  f1-score   support

           0       0.99      1.00      0.99       208
           1       0.00      0.00      0.00         3

    accuracy                           0.98       211
   macro avg       0.49      0.50      0.50       211
weighted avg       0.97      0.98      0.98       211

2025-07-24 13:54:14,033 - INFO -   🔹 [Subnó] Sexism - Avaliando 211 exemplos condicionados
2025-07-24 13:54:14,041 - INFO - 📊 Relatório para 'Sexism':
              precision    recall  f1-score   support

           0       0.86      0.69      0.77       133
           1       0.61      0.81      0.69        78

    accuracy                           0.73       211
   macro avg       0.73      0.75      0.73       211
weighted avg       0.77      0.73      0.74       211

2025-07-24 13:54:14,462 - INFO -   🔹 [Subnó] Body - Avaliando 211 exemplos condicionados
2025-07-24 13:54:14,470 - INFO - 📊 Relatório para 'Body':
              precision    recall  f1-score   support

           0       0.99      0.96      0.97       183
           1       0.76      0.93      0.84        28

    accuracy                           0.95       211
   macro avg       0.88      0.94      0.91       211
weighted avg       0.96      0.95      0.95       211

2025-07-24 13:54:14,749 - INFO -   🔹 [Subnó] Ideology - Avaliando 211 exemplos condicionados
2025-07-24 13:54:14,757 - INFO - 📊 Relatório para 'Ideology':
              precision    recall  f1-score   support

           0       0.99      0.96      0.97       206
           1       0.20      0.40      0.27         5

    accuracy                           0.95       211
   macro avg       0.59      0.68      0.62       211
weighted avg       0.97      0.95      0.96       211

2025-07-24 13:54:14,988 - INFO -   🔹 [Subnó] Religion - Avaliando 211 exemplos condicionados
2025-07-24 13:54:14,996 - INFO - 📊 Relatório para 'Religion':
              precision    recall  f1-score   support

           0       1.00      0.98      0.99       211
           1       0.00      0.00      0.00         0

    accuracy                           0.98       211
   macro avg       0.50      0.49      0.50       211
weighted avg       1.00      0.98      0.99       211

2025-07-24 13:54:15,284 - INFO -   🔹 [Subnó] Migrants - Avaliando 211 exemplos condicionados
2025-07-24 13:54:15,292 - INFO - 📊 Relatório para 'Migrants':
              precision    recall  f1-score   support

           0       1.00      0.99      0.99       209
           1       0.25      0.50      0.33         2

    accuracy                           0.98       211
   macro avg       0.62      0.74      0.66       211
weighted avg       0.99      0.98      0.98       211

2025-07-24 13:54:15,519 - INFO -   🔹 [Subnó] OtherLifestyle - Avaliando 211 exemplos condicionados
2025-07-24 13:54:15,528 - INFO - 📊 Relatório para 'OtherLifestyle':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00       211
           1       0.00      0.00      0.00         0

    accuracy                           1.00       211
   macro avg       0.50      0.50      0.50       211
weighted avg       1.00      1.00      1.00       211

2025-07-24 13:54:15,802 - INFO -   🔹 [Subnó] Origin - Avaliando 211 exemplos condicionados
2025-07-24 13:54:15,811 - INFO - 📊 Relatório para 'Origin':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00       211

    accuracy                           1.00       211
   macro avg       1.00      1.00      1.00       211
weighted avg       1.00      1.00      1.00       211

2025-07-24 13:54:15,812 - INFO -
🔷 [Nó] Homophobia - Treinando com 225 positivos, 3742 negativos
2025-07-24 13:54:16,149 - INFO - 
📊 Relatório para 'Homophobia':
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      1604
           1       0.90      0.63      0.74        97

    accuracy                           0.97      1701
   macro avg       0.94      0.81      0.86      1701
weighted avg       0.97      0.97      0.97      1701

2025-07-24 13:54:16,426 - INFO -   🔹 [Subnó] Homossexuals - Avaliando 68 exemplos condicionados
2025-07-24 13:54:16,436 - INFO - 📊 Relatório para 'Homossexuals':
              precision    recall  f1-score   support

           0       1.00      0.45      0.62        11
           1       0.90      1.00      0.95        57

    accuracy                           0.91        68
   macro avg       0.95      0.73      0.79        68
weighted avg       0.92      0.91      0.90        68

2025-07-24 13:54:16,437 - INFO -
🔷 [Nó] Homossexuals - Treinando com 206 positivos, 3761 negativos
2025-07-24 13:54:16,964 - INFO - 
📊 Relatório para 'Homossexuals':
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      1619
           1       0.90      0.70      0.79        82

    accuracy                           0.98      1701
   macro avg       0.94      0.85      0.89      1701
weighted avg       0.98      0.98      0.98      1701

2025-07-24 13:54:17,338 - INFO -   🔹 [Subnó] Gays - Avaliando 63 exemplos condicionados
2025-07-24 13:54:17,346 - INFO - 📊 Relatório para 'Gays':
              precision    recall  f1-score   support

           0       0.97      0.98      0.97        59
           1       0.67      0.50      0.57         4

    accuracy                           0.95        63
   macro avg       0.82      0.74      0.77        63
weighted avg       0.95      0.95      0.95        63

2025-07-24 13:54:17,639 - INFO -   🔹 [Subnó] Lesbians - Avaliando 63 exemplos condicionados
2025-07-24 13:54:17,647 - INFO - 📊 Relatório para 'Lesbians':
              precision    recall  f1-score   support

           0       1.00      0.17      0.29         6
           1       0.92      1.00      0.96        57

    accuracy                           0.92        63
   macro avg       0.96      0.58      0.62        63
weighted avg       0.93      0.92      0.89        63

2025-07-24 13:54:17,648 - INFO - 
🔷 [Nó] Racism - Treinando com 66 positivos, 3901 negativos
2025-07-24 13:54:18,210 - INFO - 
📊 Relatório para 'Racism':
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      1673
           1       0.40      0.07      0.12        28

    accuracy                           0.98      1701
   macro avg       0.69      0.53      0.56      1701
weighted avg       0.98      0.98      0.98      1701

2025-07-24 13:54:18,618 - INFO -   🔹 [Subnó] Black.people - Avaliando 5 exemplos condicionados
2025-07-24 13:54:18,627 - INFO - 📊 Relatório para 'Black.people':
              precision    recall  f1-score   support

           0       1.00      0.67      0.80         3
           1       0.67      1.00      0.80         2

    accuracy                           0.80         5
   macro avg       0.83      0.83      0.80         5
weighted avg       0.87      0.80      0.80         5

2025-07-24 13:54:18,628 - INFO -
🔷 [Nó] Ideology - Treinando com 64 positivos, 3903 negativos
2025-07-24 13:54:19,063 - INFO - 
📊 Relatório para 'Ideology':
              precision    recall  f1-score   support

           0       0.99      0.99      0.99      1673
           1       0.21      0.11      0.14        28

    accuracy                           0.98      1701
   macro avg       0.60      0.55      0.57      1701
weighted avg       0.97      0.98      0.98      1701

2025-07-24 13:54:19,428 - INFO -   🔹 [Subnó] Left.wing.ideology - Avaliando 14 exemplos condicionados
2025-07-24 13:54:19,436 - INFO - 📊 Relatório para 'Left.wing.ideology':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        14

    accuracy                           1.00        14
   macro avg       1.00      1.00      1.00        14
weighted avg       1.00      1.00      1.00        14

2025-07-24 13:54:19,751 - INFO -   🔹 [Subnó] Feminists - Avaliando 14 exemplos condicionados
2025-07-24 13:54:19,759 - INFO - 📊 Relatório para 'Feminists':
              precision    recall  f1-score   support

           0       1.00      0.09      0.17        11
           1       0.23      1.00      0.38         3

    accuracy                           0.29        14
   macro avg       0.62      0.55      0.27        14
weighted avg       0.84      0.29      0.21        14

2025-07-24 13:54:19,760 - INFO -
🔷 [Nó] Sexism - Treinando com 470 positivos, 3497 negativos
2025-07-24 13:54:20,167 - INFO - 
📊 Relatório para 'Sexism':
              precision    recall  f1-score   support

           0       0.92      0.97      0.94      1499
           1       0.58      0.36      0.45       202

    accuracy                           0.89      1701
   macro avg       0.75      0.66      0.69      1701
weighted avg       0.88      0.89      0.88      1701

2025-07-24 13:54:20,503 - INFO -   🔹 [Subnó] Women - Avaliando 125 exemplos condicionados
2025-07-24 13:54:20,511 - INFO - 📊 Relatório para 'Women':
              precision    recall  f1-score   support

           0       0.86      0.54      0.67        68
           1       0.62      0.89      0.73        57

    accuracy                           0.70       125
   macro avg       0.74      0.72      0.70       125
weighted avg       0.75      0.70      0.70       125

2025-07-24 13:54:20,848 - INFO -   🔹 [Subnó] Men - Avaliando 125 exemplos condicionados
2025-07-24 13:54:20,856 - INFO - 📊 Relatório para 'Men':
              precision    recall  f1-score   support

           0       0.96      0.97      0.97       112
           1       0.75      0.69      0.72        13

    accuracy                           0.94       125
   macro avg       0.86      0.83      0.84       125
weighted avg       0.94      0.94      0.94       125

2025-07-24 13:54:21,175 - INFO -   🔹 [Subnó] Feminists - Avaliando 125 exemplos condicionados
2025-07-24 13:54:21,183 - INFO - 📊 Relatório para 'Feminists':
              precision    recall  f1-score   support

           0       0.98      0.95      0.97       119
           1       0.40      0.67      0.50         6

    accuracy                           0.94       125
   macro avg       0.69      0.81      0.73       125
weighted avg       0.95      0.94      0.94       125

2025-07-24 13:54:21,427 - INFO -   🔹 [Subnó] Transexuals - Avaliando 125 exemplos condicionados
2025-07-24 13:54:21,436 - INFO - 📊 Relatório para 'Transexuals':
              precision    recall  f1-score   support

           0       0.99      1.00      1.00       124
           1       0.00      0.00      0.00         1

    accuracy                           0.99       125
   macro avg       0.50      0.50      0.50       125
weighted avg       0.98      0.99      0.99       125

2025-07-24 13:54:21,437 - INFO -
🔷 [Nó] Transexuals - Treinando com 8 positivos, 3959 negativos
2025-07-24 13:54:21,682 - INFO - 
📊 Relatório para 'Transexuals':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      1695
           1       0.00      0.00      0.00         6

    accuracy                           1.00      1701
   macro avg       0.50      0.50      0.50      1701
weighted avg       0.99      1.00      0.99      1701

2025-07-24 13:54:21,967 - INFO -   🔹 [Subnó] Trans.women - Avaliando 1 exemplos condicionados
2025-07-24 13:54:21,975 - INFO - 📊 Relatório para 'Trans.women':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         1

    accuracy                           1.00         1
   macro avg       1.00      1.00      1.00         1
weighted avg       1.00      1.00      1.00         1

2025-07-24 13:54:21,976 - INFO -
🔷 [Nó] Women - Treinando com 392 positivos, 3575 negativos
2025-07-24 13:54:22,471 - INFO - 
📊 Relatório para 'Women':
              precision    recall  f1-score   support

           0       0.94      0.98      0.96      1549
           1       0.61      0.36      0.45       152

    accuracy                           0.92      1701
   macro avg       0.77      0.67      0.70      1701
weighted avg       0.91      0.92      0.91      1701

2025-07-24 13:54:22,760 - INFO -   🔹 [Subnó] Trans.women - Avaliando 89 exemplos condicionados
2025-07-24 13:54:22,769 - INFO - 📊 Relatório para 'Trans.women':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        89

    accuracy                           1.00        89
   macro avg       1.00      1.00      1.00        89
weighted avg       1.00      1.00      1.00        89

2025-07-24 13:54:23,076 - INFO -   🔹 [Subnó] Fat.women - Avaliando 89 exemplos condicionados
2025-07-24 13:54:23,086 - INFO - 📊 Relatório para 'Fat.women':
              precision    recall  f1-score   support

           0       0.96      0.82      0.89        66
           1       0.64      0.91      0.75        23

    accuracy                           0.84        89
   macro avg       0.80      0.87      0.82        89
weighted avg       0.88      0.84      0.85        89

2025-07-24 13:54:23,451 - INFO -   🔹 [Subnó] Ugly.women - Avaliando 89 exemplos condicionados
2025-07-24 13:54:23,459 - INFO - 📊 Relatório para 'Ugly.women':
              precision    recall  f1-score   support

           0       0.94      0.93      0.93        69
           1       0.76      0.80      0.78        20

    accuracy                           0.90        89
   macro avg       0.85      0.86      0.86        89
weighted avg       0.90      0.90      0.90        89

2025-07-24 13:54:23,805 - INFO -   🔹 [Subnó] Lesbians - Avaliando 89 exemplos condicionados
2025-07-24 13:54:23,812 - INFO - 📊 Relatório para 'Lesbians':
              precision    recall  f1-score   support

           0       0.99      1.00      0.99        88
           1       0.00      0.00      0.00         1

    accuracy                           0.99        89
   macro avg       0.49      0.50      0.50        89
weighted avg       0.98      0.99      0.98        89

2025-07-24 13:54:23,816 - INFO -
🔷 [Nó] Body - Treinando com 126 positivos, 3841 negativos
2025-07-24 13:54:24,327 - INFO - 
📊 Relatório para 'Body':
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      1663
           1       0.76      0.68      0.72        38

    accuracy                           0.99      1701
   macro avg       0.88      0.84      0.86      1701
weighted avg       0.99      0.99      0.99      1701

2025-07-24 13:54:24,917 - INFO -   🔹 [Subnó] Fat.people - Avaliando 34 exemplos condicionados
2025-07-24 13:54:24,926 - INFO - 📊 Relatório para 'Fat.people':
              precision    recall  f1-score   support

           0       0.00      0.00      0.00        10
           1       0.71      1.00      0.83        24

    accuracy                           0.71        34
   macro avg       0.35      0.50      0.41        34
weighted avg       0.50      0.71      0.58        34

2025-07-24 13:54:25,410 - INFO -   🔹 [Subnó] Ugly.people - Avaliando 34 exemplos condicionados
2025-07-24 13:54:25,418 - INFO - 📊 Relatório para 'Ugly.people':
              precision    recall  f1-score   support

           0       0.85      0.73      0.79        15
           1       0.81      0.89      0.85        19

    accuracy                           0.82        34
   macro avg       0.83      0.81      0.82        34
weighted avg       0.83      0.82      0.82        34

2025-07-24 13:54:25,419 - INFO -
🔷 [Nó] Ugly.people - Treinando com 109 positivos, 3858 negativos
2025-07-24 13:54:25,784 - INFO - 
📊 Relatório para 'Ugly.people':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      1679
           1       0.81      0.77      0.79        22

    accuracy                           0.99      1701
   macro avg       0.90      0.89      0.89      1701
weighted avg       0.99      0.99      0.99      1701

2025-07-24 13:54:26,142 - INFO -   🔹 [Subnó] Ugly.women - Avaliando 21 exemplos condicionados
2025-07-24 13:54:26,149 - INFO - 📊 Relatório para 'Ugly.women':
              precision    recall  f1-score   support

           0       0.00      0.00      0.00         5
           1       0.76      1.00      0.86        16

    accuracy                           0.76        21
   macro avg       0.38      0.50      0.43        21
weighted avg       0.58      0.76      0.66        21

2025-07-24 13:54:26,150 - INFO -
🔷 [Nó] Fat.people - Treinando com 125 positivos, 3842 negativos
2025-07-24 13:54:26,437 - INFO - 
📊 Relatório para 'Fat.people':
              precision    recall  f1-score   support

           0       0.99      0.99      0.99      1666
           1       0.71      0.69      0.70        35

    accuracy                           0.99      1701
   macro avg       0.85      0.84      0.84      1701
weighted avg       0.99      0.99      0.99      1701

2025-07-24 13:54:26,699 - INFO -   🔹 [Subnó] Fat.women - Avaliando 34 exemplos condicionados
2025-07-24 13:54:26,707 - INFO - 📊 Relatório para 'Fat.women':
              precision    recall  f1-score   support

           0       0.00      0.00      0.00        12
           1       0.65      1.00      0.79        22

    accuracy                           0.65        34
   macro avg       0.32      0.50      0.39        34
weighted avg       0.42      0.65      0.51        34

2025-07-24 13:54:26,708 - INFO -
🔷 [Nó] Migrants - Treinando com 57 positivos, 3910 negativos
2025-07-24 13:54:27,001 - INFO - 
📊 Relatório para 'Migrants':
              precision    recall  f1-score   support

           0       0.99      0.99      0.99      1676
           1       0.14      0.12      0.13        25

    accuracy                           0.98      1701
   macro avg       0.56      0.55      0.56      1701
weighted avg       0.97      0.98      0.98      1701

2025-07-24 13:54:27,130 - INFO -   🔹 [Subnó] Immigrants - Avaliando 22 exemplos condicionados
2025-07-24 13:54:27,138 - INFO - 📊 Relatório para 'Immigrants':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        22

    accuracy                           1.00        22
   macro avg       1.00      1.00      1.00        22
weighted avg       1.00      1.00      1.00        22

2025-07-24 13:54:27,446 - INFO -   🔹 [Subnó] Refugees - Avaliando 22 exemplos condicionados
2025-07-24 13:54:27,454 - INFO - 📊 Relatório para 'Refugees':
              precision    recall  f1-score   support

           0       1.00      0.05      0.10        19
           1       0.14      1.00      0.25         3

    accuracy                           0.18        22
   macro avg       0.57      0.53      0.17        22
weighted avg       0.88      0.18      0.12        22

2025-07-24 13:54:27,455 - INFO -
🔷 [Nó] Religion - Treinando com 21 positivos, 3946 negativos
2025-07-24 13:54:27,703 - INFO - 
📊 Relatório para 'Religion':
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      1692
           1       0.12      0.11      0.12         9

    accuracy                           0.99      1701
   macro avg       0.56      0.55      0.56      1701
weighted avg       0.99      0.99      0.99      1701

2025-07-24 13:54:27,851 - INFO -   🔹 [Subnó] Islamists - Avaliando 8 exemplos condicionados
2025-07-24 13:54:27,859 - INFO - 📊 Relatório para 'Islamists':
              precision    recall  f1-score   support

           0       1.00      0.38      0.55         8
           1       0.00      0.00      0.00         0

    accuracy                           0.38         8
   macro avg       0.50      0.19      0.27         8
weighted avg       1.00      0.38      0.55         8

2025-07-24 13:54:28,003 - INFO -   🔹 [Subnó] Muslims - Avaliando 8 exemplos condicionados
2025-07-24 13:54:28,011 - INFO - 📊 Relatório para 'Muslims':
              precision    recall  f1-score   support

           0       1.00      0.71      0.83         7
           1       0.33      1.00      0.50         1

    accuracy                           0.75         8
   macro avg       0.67      0.86      0.67         8
weighted avg       0.92      0.75      0.79         8
```

