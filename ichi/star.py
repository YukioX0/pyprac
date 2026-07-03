def user_input():
    n = int(input ("Enter the no of rows : "));
    execute = print_stars(n);
    return n;

def print_stars(n):
    for i in range (n):
        for j in range (i):
            print ("*", end = " ");
        print ();

n = user_input();