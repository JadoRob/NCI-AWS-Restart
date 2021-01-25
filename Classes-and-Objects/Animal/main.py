import os 
from os import system
from animal import Animal

system('clear')

animalList = []

number_of_animals = int(input('How many animals do you want to create? >>'))
print('Nice!! {number_of_animals} animals')
print('Here we go!')

type_of_animal = input('what is the animal? >> ')
for a in range(number_of_animals):
    animal = Animal()
    print(f'-------- {str.upper(type_of_animal)} # {a + 1} --------')
    breed = str(input('What is the breed of your {type_of_animal}? >> '))
    animal.setBreed(breed)
    name = str(input(f'What is the name of your {type_of_animal}? >> '))
    animal.setName(name)
    animalList.append(animal)

animalCounter = 1
for animal in animalList:
    print(f'Animal # {animalCounter}')
    print(f'''
    Breed......{animal.getBreed()}
    Name.......{animal.getName()}
    ''')
    animalCounter += 1