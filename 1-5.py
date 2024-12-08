# An array contains values: 1, 2, 3, 4, 5.
# Write a program that modifies the array values.
# Print the array after each change.

# subtract one from the first element of the array
# increase the last array element by 4
# multiple the middle array element by 2
# Sample result:
# Array: [1,2,3,4,5]
# Array: [0,2,3,4,5]
# Array: [0,2,3,4,9]
# Array: [0,2,6,4,9]

arr = [1,2,3,4,5]
print(arr)

# subtract one from the first element of the array
arr[0] = arr[0] - 1
print(arr)

# increase the last array element by 4
arr[-1] = arr[-1] + 4 
print(arr)

# multiple the middle array element by 2
arr[int(len(arr)/2)] = arr[int(len(arr)/2)] * 2
print(arr)