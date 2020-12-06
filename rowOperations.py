import numpy as np
import operator
import fractions
import copy as cp

def printMatrix():
    for i in matrix:
        print('[\t',end='')
        for j in i:
            print(j, '\t', end='')
        print(']')


def eliminateColumn(row, col, j):
    midop = '-'
    secondCoef = matrix[j][col]
    firstCoef = matrix[row][col]
    if firstCoef != 0 and secondCoef != 0:
        matrix[j] = firstCoef*matrix[j] - secondCoef*matrix[row]
        if str(firstCoef)[0] == '-':
            firstCoef *= -1
            secondCoef *= -1

        if str(secondCoef)[0] == '-':
            secondCoef *= -1
            midop = '+'

        if firstCoef == 1:
            firstCoef = ''

        if secondCoef == 1:
            secondCoef = ''
            
        print(f"\n{firstCoef}R{j+1} {midop} {secondCoef}R{row+1}\n")
        printMatrix()

def swapPivot(row, j):
    temp = cp.copy(matrix[row])
    matrix[row] = cp.copy(matrix[j])
    matrix[j] = cp.copy(temp)
    print(f"\nR{row+1} -> R{j+1}\n")
    printMatrix()

def reducePivot(row, col):
    print(f"\nR{row+1} * {1/matrix[row][col]}\n")
    matrix[row] = matrix[row] / matrix[row][col]
    printMatrix()

def calculateRREF():
    row = 0
    col = 0
    printMatrix()
    while col < len(matrix[0]) and row < len(matrix):
        if matrix[row][col] == 0:
            for j in range(row+1, len(matrix)):
                if matrix[j][col] == 1:
                    swapPivot(row, j)
                    for j in range(len(matrix)):
                        if row == j:
                            continue
                        eliminateColumn(row, col, j)
                    row += 1
                    break
            else:
                for j in range(row+1, len(matrix)):
                    if matrix[j][col] != 0:
                        swapPivot(row, col)
                        if matrix[row][col] != 1:
                            reducePivot(row, col)
                        for j in range(len(matrix)):
                            if row == j:
                                continue
                            eliminateColumn(row, col, j)
                        row += 1
                        break
        else:
            if matrix[row][col] != 1:
                reducePivot(row, col)
            for j in range(len(matrix)):
                if row == j:
                    continue
                eliminateColumn(row, col, j)
            row += 1  
        
        col += 1

def calculateREF():
    col = 0
    row = 0
    printMatrix()
    while col < len(matrix[0]) and row < len(matrix):
        if matrix[row][col] == 0:
            for j in range(row+1, len(matrix)):
                if matrix[j][col] != 0:
                    swapPivot(row, j)
                    for j in range(row+1, len(matrix)):
                        eliminateColumn(row, col, j)
                    row += 1
                    break
                    
        else:
            for j in range(row+1, len(matrix)):
                eliminateColumn(row, col, j)
            row += 1

        col += 1

def rowOperation():
    operation = input("\nEnter 'stop', 'ref', 'rref' or the row operation you want to apply: ")
    if operation == 'stop':
        return False
    elif operation == 'ref':
        calculateREF()
        return True
    elif operation == 'rref':
        calculateRREF()
        return True

    try:
        operation = operation.split(' ')
        first = operation[0].split('R')

        if first[0] == '':
            first[0] = '1'
        first[0] = fractions.Fraction(first[0])
        first[1] = int(first[1])
        arg1 = matrix[int(first[1])-1] * first[0]
        
        if operation[1] == '*' or operation[1] == '/':
            arg2 = int(operation[2])

        else:
            second = operation[2].split('R')
            if second[0] == '':
                second[0] = '1'
            second[0] = fractions.Fraction(second[0])
            second[1] = int(second[1])
            arg2 = matrix[second[1]-1] * second[0]

        if operation[1] == '->':
            print(arg1, arg2)
            matrix[first[1]-1] = arg2
            matrix[second[1]-1] = arg1
        else:
            matrix[first[1]-1] = ops[operation[1]](arg1, arg2)
        
        printMatrix()
    except IndexError:
        print("That row doesn't exists.")
    except ValueError:
        print("Incorrect Syntax for Row Operations. Make sure you are following the correct syntax mentioned above.")

    return True

    
def main():
    global ops, matrix
    ops = { '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv }
    matrix = []
    try:
        x = int(input("Enter number of rows: "))
        y = int(input("Enter number of columns: "))

        for i in range(x):
            while True:
                elements = input(f"Enter elements of ROW {i+1} with spaces: ").split(' ')
                elements = [fractions.Fraction(i) for i in elements if i != ""]
                break
            
            for j in range(y-len(elements)):
                elements.append(0)
            for j in range(len(elements)-y):
                elements.pop()
            matrix.append(elements)

        matrix = np.array(matrix)
        print('\nFollow the syntax below to apply row operations\n2R1 + R2\tMultiplies R1 by 2 and adds R2\nR1 * 4\t\tMultiplies R1 by 4\nR1 / 3\t\tDivides R1 by 3\nR1 -> R2\tSwaps R1 with R2\n')
        printMatrix()

        while rowOperation():
            pass

    except ValueError:
        print("Invalid value. Only numbers are allowed.")
        main()
    

if __name__ == '__main__':
    main()