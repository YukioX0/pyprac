def print_inverted_stars(n):
    for i in range (0, n):
        for j in range (0, n-i):
            print ("*", end = " ");
        print ();

def user_input():
    n = int(input ("Enter the no of rows : "));
    execute = print_inverted_stars(n);
    return n;


n = user_input();