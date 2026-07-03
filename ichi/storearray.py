#I want to write a program to store an array of numbers and perform various operations on it, such as finding the sum, average, maximum, and minimum values. 
# The program should allow the user to input the numbers and then choose which operation they want to perform on the array. 

def store_array():
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    for i in range(n):
        num = float(input("Enter nums: "))
        arr.append(num)
    return arr

arr = store_array()
print("Array:", arr)
print("sorted array: ", sorted(arr))
print("bubble sort: ", )