length = int(input('Enter the length : '))
breadth = int(input('Enter the breadth : '))

area = length * breadth
perimeter = 2*(length + breadth)
diagonal = (length**2 + breadth**2)**(0.5)

print("Area = ", area)
print('Perimeter = ', perimeter)
print('Diagonal = ', diagonal)
