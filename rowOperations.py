import numpy as np
import operator

ops = { "+": operator.add, "-": operator.sub}
matrix = []

def rowOperation():
    operation = input("Enter 'stop' or the row operation you want to apply(e.g R2 + 2R1): ")
    if operation == 'stop':
        return False
    operation = operation.split(' ')
    first = operation[0].split('R')
    second = operation[2].split('R')
    
    if first[0] == '':
        first[0] = '1'
    if second[0] == '':
        second[0] = '1'
        
    first = [int(i) for i in first]
    second = [int(i) for i in second]
    try:
        arg1 = matrix[first[1]-1] * first[0]
        arg2 = matrix[second[1]-1] * second[0]
        matrix[first[1]-1] = ops[operation[1]](arg1, arg2)
    except IndexError:
        print("That row doesn't exists.")
    print(matrix)
    return True
    
x = int(input("Enter number of rows: "))
y = int(input("Enter number of columns: "))

for i in range(x):
    elements = input(f"Enter elements of ROW {i+1} with spaces: ").split(' ')
    elements = [int(i) for i in elements]
    
    for j in range(y-len(elements)):
        elements.append(0)
    for j in range(len(elements)-y):
        elements.pop()
    matrix.append(elements)

matrix = np.array(matrix)
print(matrix)
while rowOperation():
    pass