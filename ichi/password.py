def strong(p):
    if len(p)>= 8:
        print("Strong Password")
    else:
        print("Weak Password");

def user_input():
    p = input ("Enter the password : ");
    execute = strong(p);
    return p;

user_input();
