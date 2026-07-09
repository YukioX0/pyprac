#5. Mixed (String + Logical)
#Take a string from user.
#Check if:
# - The string length is greater than 5
# - AND it starts with 'A' or 'a'
# Print "Valid String" or "Invalid String"

x = input("Enter a string: ")

def check():
    if len(x) > 5 and (x.startswith('A') or x.startswith('a')):
        print("Valid String")
    else:
        print("Invalid String")

check()

# 3. String Operations
# Take your city name as input.
# Print the following:
# 1. City name in reverse order
# 2. Number of vowels in the city name (a,e,i,o,u)
# 3. City name without first and last character

city = input("enter your city name: ")
city = []

def rev():
    return 