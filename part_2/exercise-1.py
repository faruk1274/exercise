# TITLE: Programming terminology
# The following program contains several syntactic errors. Please fix the program so that the syntax is in order and the program works as specified by the examples below.

#   number = input("Please type in a number: ")
#   if number>100
#     print("The number was greater than one hundred")
#     number - 100
#     print("Now its value has decreased by one hundred)
#      print("Its value is now"+ number)
#  print(number + " must be my lucky number!")
#  print("Have a nice day!)

# ++++ CORRECTIONS ++++
number = input('please type in a number: ')
if number > 100:
    print('The number was greater than one hundred')
    number - 100
    print("Now its value has decreased by one hundred)
    print(f"Its value is now {number}")
print(f"{number} must be my lucky number!")
print("Have a nice day!)

#(2) Number of characters
word = "abcd"
print(len(word))

print(len("hi there"))

word2 = "howdydoody"
length = len(word2)
print(length)

empty_string = ""
length = len(empty_string)
print(length)

#(3) Typecasting

temperature = float(input("Please type in a temperature: "))

print("The temperature is", temperature)

print("...and rounded down it is", int(temperature))