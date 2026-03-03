'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 5 Assignment 2
'''
def check_password(password):
    if len(password) >=8:
        return "Password accepted."
    else:     
        return "Password too short."
    
    user_password = input("Enter a password: ")
    
    result = check_password(user_password)      
    print(result)