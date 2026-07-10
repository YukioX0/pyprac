# Given a string s, the task is to check if it is palindrome or not.
def is_palindrome(s):
#first i will define left and right variables for the string
    left = 0
    right = len(s) - 1
#now iterate through the string
    while left < right: 
        if s[left] != s[right]:
            return"string is not palindrome"
        left += 1
        right -= 1

    return"string is palindrome"

s = input("Enter a string: ")
print(is_palindrome(s))