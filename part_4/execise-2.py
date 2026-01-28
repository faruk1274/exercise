# TITILE: Lists
# (1) Change the value of an item
index = [1, 2, 3, 4, 5]
print(index)
index[1] = 7
print(index)

# (2)Palindromes
def palindromes(text):
    return text == text[::-1]

print(palindromes("madam"))