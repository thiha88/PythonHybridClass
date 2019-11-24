#week5 24.11.2019

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
# [1, 66.25, 333, 333, 1234.5]

del a[:] # delete from start to end
del [:4]
del [3:]

>>> t = 1, (2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> u = t, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> u
((1, (2, 3, 4, 5, 6, 7, 8, 9, 10)), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
>>> u[0]
(1, (2, 3, 4, 5, 6, 7, 8, 9, 10))
>>> u[0] = 3, 4, 5, 6, 7, 8
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> u[0] = 7, (3, 4, 5, 6, 7, 8, 9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t[0] = 12345
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>

# len -> length

>>> empty = ()
>>> singleton = 'hello'
>>> len(singleton)
5
>>> len(empty)
0
>>> singleton = 'hello', 'world'
>>> len(singleton)
2

= ,
= ()
= [()]
= []
= {}

>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)
{'orange', 'pear', 'apple', 'banana'}
>>> basket = {'banana', 'apple', 'cucumber', 'pineapple', 'orange', 'grape', 'apple', 'banana'}
>>> print(basket)
{'banana', 'grape', 'pineapple', 'apple', 'orange', 'cucumber'}
>>> print(basket)
{'banana', 'grape', 'pineapple', 'apple', 'orange', 'cucumber'}
>>> 'orange' in basket
True
>>> 'crabgrass' in basket
False

>>> a = set('mgmgmamamyamyaayeaye')
>>> a
{'e', 'm', 'y', 'a', 'g'}
>>> b = set('kokoaungaungkyikyikyukyu')
>>> b
{'k', 'u', 'o', 'y', 'n', 'a', 'g', 'i'}
>>> c = set('1234567890')
>>> c
{'4', '3', '9', '8', '6', '7', '1', '5', '2', '0'}
>>> a - b
{'m', 'e'}
>>> a - b
{'m', 'e'}
>>> a
{'e', 'm', 'y', 'a', 'g'}
>>> b
{'k', 'u', 'o', 'y', 'n', 'a', 'g', 'i'}
>>> a - b
{'m', 'e'}
>>> a | b
{'k', 'e', 'u', 'o', 'm', 'y', 'n', 'a', 'g', 'i'}
>>> a & b
{'a', 'g', 'y'}
>>> a ^ b
{'k', 'e', 'u', 'o', 'm', 'n', 'i'}
>>> b - a
{'k', 'u', 'o', 'n', 'i'}
>>> b | a
{'k', 'e', 'u', 'o', 'm', 'y', 'n', 'a', 'g',
