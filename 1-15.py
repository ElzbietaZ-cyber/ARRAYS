# Define a function that sorts an array of numbers using the bubble sort
# algorithm. Use the information in the pseudocode provided earlier.
# Then, write a program that sorts the following collections of data:

# Here is the bubble sort algorithm expressed in pseudocode,
# a universal notation that is independent of the programming language:

# procedure bubbleSort(arr):
#    n = length(arr)
#    for i = 0 to n-1:
#       for j = 0 to n-i-2:
#          if arr[j] > arr[j+1]:
#                swap arr[j] and arr[j+1]
#    return arr


car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

###
# Bubble sort
#
def bubble_sort(arr):

   for i in range(len(arr)-1):
      for j in range(len(arr)-1-i-2):
         if arr[j] > arr[j+1]:
            z = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = z


   return arr

print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)