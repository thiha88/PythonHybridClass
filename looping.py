knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

animals = ['bear', 'polar', 'tiger']
for q, a, a in zip(questions, answers, animals):
    print('What is your {0}? It is {1}. It is {2}.'.format(q, a, a))

for i in reversed(range(1, 10, 2)):
    print(i)

for i in reversed(range(10, 99, 3)):
    print(i)

for i in reversed(range(0, -100, 3)):
    print(i)

for i in reversed(range(-100, 0, 3)):
    print(i)

for i in reversed(range(-100, 10, 3)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data

>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'

>>> string1, string2, string3 = '1', '2', '3'
>>> number = string1 or string2 or string3
>>> number
'1'

>>> string1, string2, string3 = '', '', '3'
>>> number = string1 or string2 or string3
>>> number
'3'

# (1, 2, 3)              < (1, 2, 4)
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, -1)
# (1, 2, 3)             == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

>>> 'ABC' < 'C' < 'Pascal' < 'Python'
True
>>> (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
True
>>>
