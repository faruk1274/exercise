# TITLE: Information from the user

#(1) Please write a program which asks for the user's name and then prints it twice, on two consecutive lines.
name = input('enter your name: ')
print(name)
print(name)

#(2) 
name = input('your name: ')
print('!',name,'!',name,'!')

#(3) Please write a program which asks for the user's name and address. The program should also print out the given information, as follows
name = input('enter your name')
address = input('enter your address')
print('name: ' + name)
print('Street address: ' + address)

#(4) Here is a program which should ask for three utterances and print them out, like so:
first  = input('The 1st part: ')
second = input('The 2st part: ')
third = input('The 3st part: ')
print(f"{first}-{second}-{third}")

#(5) Please write a program which prints out the following story. The user gives a name and a year, which should be inserted into the printout.
name = input('Please type in a name')
year = input('Please type in a year')
print(f"{name}is a valiant knight, born in the year {year}. One morning{name} woke up to an awful racket: a dragon was approaching the village. Only {name} could save the village's residents.")
