# TITLE 

# (1)String multiplied
name = input('Please type in a string')
num = int(input('Please type in a string'))
print(name*num)

# (2) End to beginning

name = input('End to beginning')
index = 0
while index < len(name):
    print(name[-index])
    index += 1

# (3)A line of hashes
width = int(input('width'))
print('#'*width)

# (4)Right-aligned
text = input("Please type in a string: ")

if len(text) < 20:
    stars = "*" * (20 - len(text))
    text = stars + text

print(text[:20])

# (5) A framed word

text = input("Please type in a string: ")

frame_width = 30
inner_width = frame_width - 2  # space between the side *

# Center the text inside the frame
padding_left = (inner_width - len(text)) // 2
padding_right = inner_width - len(text) - padding_left

print("*" * frame_width)
print("*" + " " * padding_left + text + " " * padding_right + "*")
print("*" * frame_width)