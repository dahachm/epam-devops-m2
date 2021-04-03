# Task 1

# Self-study input() function. 
# Write a script which accepts a sequence of comma-separated numbers from user 
# and generate a list and a tuple with those numbers and prints these objects 
# as-is (just print(list) without any formatting).

input_str = input('Enter some comma-separated numbers: ')

mylist = [float(i) for i in input_str.split(',')]

mytuple = tuple(float(i) for i in input_str.split(','))

print()
print(type(mylist), ':')
print(mylist)

print()
print(type(mytuple), ':')
print(mytuple)


# input() function returns string value.
# Here is list comprehension used to create a list and tuple from array of comma-separated 
# strings produced by *input_str.split(',')*
# These small string are converted into float type