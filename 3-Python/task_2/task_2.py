# Task 2

# Develop a procedure to print all even numbers from a numbers list which is given as an argument. 
# Keep the original order of numbers in list and stop printing if a number 254 was met. 
# Don't forget to add a check of the passed argument type.

def printEven(numbers):

    print('printEven:', end='\n\t')
    try:
        for i in numbers:
            if (i % 2 == 0):
                print(i, end=' ')
            if (i == 254):
                print()
                return
        print()
        return
    except Exception as errorMsg:
        print('\nERROR:', end='')
        print(errorMsg)
        return    


test_1 = [1, 2, 3, 4, 6, 456, 222, -2, 254, 10, 45]
test_2 = '[1, 2, 3, 4, 6, 456, 222, -2, 254, 10, 45]'
test_3 = [1, 2, 3, 4, 6, '456', 222, -2, 254, 10, 45]
test_4 = [254, 1, 2, 3, 4, 6, 456, 222, -2, 10, 45]
test_5 = [1, 2, 3, 4, 6, 456, 222, -2, 10, 45]

print('\n    --- Case #1 ---')
print(f'Input: {test_1} (type: {type(test_1)})')
printEven(test_1)

print('\n    --- Case #2 ---')
print('Input: ', test_2, '(type: ', type(test_2),')')
printEven(test_2)

print('\n    --- Case #3 ---')
print(f'Input: {test_3} (type: {type(test_3)})')
printEven(test_3)

print('\n    --- Case #4 ---')
print(f'Input: {test_4} (type: {type(test_4)})')
printEven(test_4)

print('\n    --- Case #5 ---')
print(f'Input: {test_5} (type: {type(test_5)})')
printEven(test_5)
