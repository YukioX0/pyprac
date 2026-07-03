# LOgic Practice
# WAP to print * when the input is given from 1 to n

n = int(input ("Enter the no of rows : "));
print (n);
''' we took the input for the no of rows and stored it in n
now we have to print stars from 1 to n 
so we will use loops '''

""" i = 1;
while i <= n:
    print ("*");
    i = i + 1;
 """



""" using for loop"""

for i in range (n):
    for j in range (i, n):
        print ("*", end = " ");
    print ();

#now I want to print the stars in the form of a triangle lets use while loop
# i = 1;
# while i <= n:
#     j = 1;
#     while j <= i:
#         print ("*", end = " ");
#         j = j + 1;
#     print ();
#     i = i + 1;