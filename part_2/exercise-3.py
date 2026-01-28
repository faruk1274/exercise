# TITLE: Combining conditions

# (1) Age check
age = int(input('What is your age? '))
if age > 10 and age <20:
    print(f"Ok, you're {age} years old")
elif age < 10 and age > 0:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")

# (2) Nephews

name = input("Please enter your name: ")

if name == "Huey" or name == "Dewey" or name == "Louie":
    print("You are one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("You are one of Mickey Mouse's nephews.")
else:
    print("I don't recognize you as one of the famous nephews.")

# (3)Grades and points

gardes = int(input("How many points [0-100]: "))
if gardes > 100:
    print('impossible')
elif gardes <= 100 or gardes >= 90:
    print('you earn 5 point')
elif gardes < 90 or gardes >=80:
    print('you earn 4 point')
elif gardes < 80 or gardes >=70:
    print('you earn 3 point')
elif gardes < 70 or gardes >=60:
    print('you earn 2 point')
elif gardes < 60 or gardes >=50:
    print('you earn 1 point')
elif gardes < 50 or gardes >=0:
    print('fail')
else:
    print('impossible!')

# (4) FizzBuzz
numbers = int(input("Number: "))
if numbers % 5 == 0:
    print('Fizz')
elif numbers % 3 == 0:
    print('Buzz')
elif numbers % 3 ==0 and numbers % 5 == 0 :
    print('FizzBuzz')

else:
    print(numbers)


# (5)Alphabetically in the middle

letter1 = input("Enter first letter: ")
letter2 = input("Enter second letter: ")
letter3 = input("Enter third letter: ")

letters = [letter1, letter2, letter3]
# Sort the letters alphabetically
letters.sort()
print("The middle letter is:", letters[1])



