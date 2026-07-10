# Given a string s, the task is to check if it is palindrome or not.
s = input("Enter a string")

def is_palindrome():
#first i will define left and right variables for the string
    left = 0
    right = -1
#now iterate through the string
    while s[left] != s[right]:
        return("string is not palindrome")
        left += 1
        right -= 1
    else right==left:
        return("string is palindrome")
    
print(is_palindrome(s))