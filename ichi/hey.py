# print("hey")
# x = input("input your number and Press Enter to continue...")
# print("you pressed Enter!", x)
# if x == "2!":
#     print("even")
# else:
#     print("odd")

n = int(input("Enter a number: "))
for i in range(n):

    print("*" * (n-i), end="-")
    print( "*" * (i+1))
   