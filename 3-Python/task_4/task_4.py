# Task 4

# Write a small script which will print a string using all the types 
# of string formatting which were considered during the lecture with the following context: 
#
#"This script has the following PID: <ACTUAL_PID_HERE>. 
# It was ran by <ACTUAL_USERNAME_HERE> to work happily on <ACTUAL_OS_NAME>-<ACTUAL_OS_RELEASE>."

import os

print("This output use f'{}{}' format:")
print(f'This script has the following PID: {os.getpid()}.')
print(f'It was ran by {os.getlogin()} to work happily on {os.uname().sysname}-{os.uname().release}.')

print()

print("This output use .format():")
print('This script has the following PID: {}.'.format(os.getpid()))
print('It was ran by {} to work happily on {}-{}.'.format(os.getlogin(), os.uname().sysname, os.uname().release))

print()

print("This output use % (modulo operator): ")
print('This script has the following PID: %d.' % (os.getpid()))
print('It was ran by %s to work happily on %s-%s.' % (os.getlogin(), os.uname().sysname, os.uname().release))