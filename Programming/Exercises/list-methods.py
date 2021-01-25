import os
from os import system

system('clear')




numbers = [3, 4, 5, 6, 2, 1, 9, 2, 0, 22, 26]
# copy the numbers list (number) into the new list (numbers1)
numbers1 = numbers.copy()
print(' ')
print('---------------- USING THE sort() METHOD ------------------')
print('List without yet invoking the sort() function: \n{}'.format(numbers))

numbers.sort()

print('List after invoking the sort() function: \n{}'.format(numbers))
print('-----------------------------------------------------------')
print(' ')

print('---------------- USING THE count() METHOD ------------------')
print(numbers)

for number in numbers:
    print('{} is counted {} times'.format(number, numbers.count(number)))

print('-----------------------------------------------------------')
print(' ')

print('---------------- USING THE copy() METHOD ------------------')
print('First list: \n{}'.format(numbers))
print('New list numbers1: \n{}'.format(numbers1))
print('-----------------------------------------------------------')
print(' ')
print('--------------- USING THE reverse() FUNCTION --------------')
print('list without yet invoking the reverse() function: \n{}'.format(numbers))

numbers.reverse()

print('List after invoking the revers() function: \n{}'.format(numbers))
print('-----------------------------------------------------------')
print(' ')
print('-------------- USING THE append() FUNCTION ----------------')
print('List without yet invoking the append() function: \n{}'.format(numbers))

numbers.append(15)

print('List after using the append() function and adding 15: \n{}'.format(numbers))
print('-----------------------------------------------------------')
print(' ')
print('-------------- USING THE insert() FUNCTION ----------------')
print('List without yet invoking the insert() function: \n{}'.format(numbers))

numbers.insert(2, 20)

print('List after invoking the insert() function: \n{}'.format(numbers))
print('-----------------------------------------------------------')
print(' ')

print('-------------- USING THE remove() FUNCTION ----------------')
print('List without yet invoking the remove() function: \n{}'.format(numbers))

numbers.remove(20)

print('List after invoking the remove() function and removing 20: \n{}'.format(numbers))
print('-----------------------------------------------------------')
print(' ')

print('-------------- USING THE pop() FUNCTION ----------------')
print('List without yet invoking the pop() function: \n{}'.format(numbers))

numbers.pop()

print('List after invoking the pop() function: \n{}'.format(numbers))
print('-----------------------------------------------------------')
print(' ')

print('------------------------ USING del ------------------------')
print('List without yet invoking del: \n{}'.format(numbers))

del numbers[2:5]

print('List after using del and deleting elements from 2 to 4 function: \n{}'.format(numbers))

del numbers[:2]

print('List after using del and deleting all elements before index 2: \n{}'.format(numbers))

del numbers[4:]

print('List after using del and deleting all elements after index 3: \n{}'.format(numbers))

print('-----------------------------------------------------------')
print(' ')

print('-------------- USING THE clear() FUNCTION ----------------')
print('List without yet invoking the clear() function: \n{}'.format(numbers))

numbers.clear()

print('List after invoking the clear() function: \n{}'.format(numbers))
print('-----------------------------------------------------------')
print(' ')