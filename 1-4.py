# An array contains values: 2, 3, 7, 5, 4.
# Write a program that prints:
# the array
# number of elements
# first value
# second value
# last value
# last but one value (do not use negative index values)
# sum of the first and last value
# middle value
# all array values separated by a single space (use a loop statement)

# Tip: to read the last value of an array use array[len(array)-1]
#  or array[-1]

###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Last value', arr[-1])
print('Last but one value value', arr[len(arr)-2])
print('Sum of the first value and last', arr[0] + arr[-1])
print('Middle value: ', arr[int(len(arr)/2)] )
print('All array values seperated by a single space: ')
string = ""

for index in range(len(arr)):
    string = string + str(arr[index]) + " "

print(string)
    
