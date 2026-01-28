#Please write a program which prints out an emoticon: :-)

print(": :-)")

# This program is supposed to print out the names of the 
# brothers in alphabetical order, but it's not working quite right yet.
# Please fix the program so that the names are printed in the correct order.

names = ["Simeoni","Juhani","Eero","Lauri","Aapo","Tuomas","Timo"]

for name in sorted(names):
    print(name)

     #OR

print(*sorted(["Simeoni","Juhani","Eero","Lauri","Aapo","Tuomas","Timo"]), sep="\n")

# (3) Please write a program which prints out the following lines exactly as they are written here, punctuation and all:

# Row, row, row your boat,
# Gently down the stream.
# Merrily, merrily, merrily, merrily,
# Life is but a dream.

print("Row, row, row your boat,")
print('Gently down the stream.')
print("Merrily, merrily, merrily, merrily,")
print("Life is but a dream.")

#(4) Please write a program which prints out the number of minutes in a year. Use Python code to perform the calculation, as in the previous code example.
 
minutes_in_a_year = 365 * 24 * 60
print('the number of minutes in a year')
print(minutes_in_a_year)