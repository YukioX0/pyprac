# 1. Logical Operators
# Python
# Take three subject marks from user (English, Math, Science).
# Check if the student has passed:
# All marks should be >= 40 (use 'and' operator)
# If any one subject is < 40, print "Fail"

x = int(input("Enter marks for English: "))
y = int(input("Enter marks for maths: "))
z = int(input("Enter marks for Python: "))

def result():
    if x >= 40 and y >= 40 and z >= 40:
        print("pass")
    else:
        print("fail")

result()
