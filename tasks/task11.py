""" 
Recursion Tasks:
  create a function that can generate 20 to 5 in reverse order
  create a function that will asks for user input 5 times and print after each input
"""
def num(n):
    if n<5:
        return n
    print(n)
    num(n-1)
num(20)

def user():
    for i in range(5):
        user_name = input("enter the name :")
        print(i)
user()

