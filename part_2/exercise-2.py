# TITLE: More conditionals
#(1)Age of maturity
age = int(input('enter your age: '))

if age >= 18:
    print('your are in the age of maturity.')
else:
    print('your not mature')

#(2)Greater than or equal to

first = int(input('enter your age: '))
second = int(input('enter your age: '))

if first > second:
    print(f'{first} is greater than {second}')
elif first == second:
    print('The numbers are equal!')
else:
    print(f'{second} is greater than {first}')

#(3) The elder
person1 = input('enter your age: ')
age1 = int(input('enter your age: '))

person2 = input('enter your age: ')
age2 = int(input('enter your age: '))

print('name: ',person1)
print('name: ',age1)
print('name: ',person2)
print('name: ',age2)
if age1 > age2:
    print(f'The elder is {person1}')
elif age1 == age2:
    print(f'{person1} and {person2} are the same age')

#(4) Alphabetically last
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if word1 > word2:
    printf"{word1} comes alphabetically last.")
elif word1 == word2:
    print("You gave the same word twice.")
else:
    print(f"{word2} comes alphabetically last.")
