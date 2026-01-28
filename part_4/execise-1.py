# TITLE: The Visual Studio Code editor, Python interpreter and built-in debugging tool
def shape(triangle_size, triangle_char, rectangle_height, rectangle_char):
    # Print the triangle
    for i in range(1, triangle_size + 1):
        print(triangle_char * i)

    # Print the rectangle
    for _ in range(rectangle_height):
        print(rectangle_char * triangle_size)

shape(5, "*", 3, "#")