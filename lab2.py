
#shape calculation
import math
def calculate_area(shape, dim1, dim2=0):
    if shape == 'circle':
        return math.pi * (dim1 ** 2)
    elif shape == 'rectangle':
        return dim1 * dim2
    elif shape == 'triangle':
        return 0.5 * dim1 * dim2
    elif shape == 'square':
        return dim1 * dim1
    else:
        return 'Invalid shape'


shape = input("Enter a shape, e.g. circle, rectangle, triangle, or square: ").lower()

if shape in ['circle', 'square']:
    dim1 = float(input("Enter the length (if s quare) or radius (if circle): "))
    area = calculate_area(shape, dim1)
elif shape in ['rectangle', 'triangle']:
    dim1 = float(input("Enter the length: "))
    dim2 = float(input("Enter the width (if rectangle): "))
    area = calculate_area(shape, dim1, dim2)
else:
    area = 'Invalid shape'
print(f'The area of the {shape} is: {area}')


#----------------------------------------------------------------
#character locator

def locate_character(string, character):
    index = [index for index, char in enumerate(string) if char == character]
    return index

string = input("Enter a string: ")
character = input("Enter a character to locate: ")

if len(character) != 1:
    print("Please enter a single character.")
else:
    index = locate_character(string, character)
    if index:
        print(f"The character '{character}' is found at index: {index}")
    else:
        print(f"The character '{character}' is not found in the string.")

#----------------------------------------------------------------
#Multiplication table

def multiply_table(n):
    table = [[i * j for j in range(1, i + 1)] for i in range(1, n + 1)]
    return table


n = int(input('Enter the size of the table to multiply'))

table = multiply_table(n)
for row in table:
    print(' '.join(map(str, row)))


#----------------------------------------------------------------
#Dictionry

def dictionary(names):
    name_dict = {}
    for name in names:
        first_letter = name[0].lower()
        if first_letter not in name_dict:
            name_dict[first_letter] = []
        name_dict[first_letter].append(name)
    return dict(sorted(name_dict.items()))


names = input('Enter names separating them using comma: ').split(',')

names = [name.strip() for name in names]

name_dict = dictionary(names)
print(name_dict)