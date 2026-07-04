def print_inverted_stars(n):
    for i in range (n):
        for j in range (i):
            print ("*", end = " ");
        print ();

def user_input():
    n = int(input ("Enter the no of rows : "));
    execute = print_inverted_stars(n);
    return n;


n = user_input();