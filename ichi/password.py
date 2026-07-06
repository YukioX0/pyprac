def strong(p):
    if len(p) >= 8 and '@' in p and '#' in p:
        print("Strong password")
    else:
        print("Weak password")

def user_input():
    p = input ("Enter the password : ");
    execute = strong(p);
    return p;

user_input();
