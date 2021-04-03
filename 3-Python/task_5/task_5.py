# Task 5

# Develop a function that takes a list of integers (by idea not in fact) as an argument and returns 
# list of top-three max integers. If passed list contains not just integers collect them and print the 
# following error message: You've passed some extra elements that I can't parse: [<"elem1", "elem2" .... >]. 
# If return value will have less than 3 elements for some reason it's ok and shouldn't cause any problem, but 
# some list should be returned in any case.

def top3Max(list):
    try:
        extras  = []
        numbers = []
        topNum  = []
        for i in list:
            if isinstance(i, int) or isinstance(i, float):
                numbers.append(i)
            else:
                extras.append(i)
        numbers.sort()       
        if len(numbers) > 0:
            print('Top max numbers:', end='\n\t')
            for i in range(0, min(3, len(numbers))):
                print(numbers[len(numbers)-i-1], end=' ')
                topNum.append(numbers[len(numbers)-i-1])
        else:
            print('There is no numbers in the list!')
        if len(extras) > 0:
            print("\nYou've passed some extra elements that I can't parse:", end="\n\t")
            for i in extras:
                print(i, end=' ')           
    except Exception as errorMsg:
        print('ERROR in top3Max(): '+ str(errorMsg))
    finally:
        print('\n')
        return topNum, extras     

test_1 = [1, 10, 45, 3, 333]
test_2 = [2, 10, '20']
test_3 = ['200_', '300_', '63_']
test_4 = 'str'
test_5 = 5

print('  --- TEST #1 --- ')
print('Input: ' + str(test_1))
top3Max(test_1)

print('  --- TEST #2 --- ')
print('Input: ' + str(test_2))
top3Max(test_2)

print('  --- TEST #3 --- ')
print('Input: ' + str(test_3))
top3Max(test_3)

print('  --- TEST #4 --- ')
print('Input: ' + str(test_4))
top3Max(test_4)

print('  --- TEST #5 --- ')
print('Input: ' + str(test_5))
top, extras = top3Max(test_5)
print (top)
print (extras)