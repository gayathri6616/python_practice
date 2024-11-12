"""
convert the following functions into anonymous functions
"""
def homepage(name, bank):
    return f"Hey {name}, Happy {bank} Banking"

def isNegative(num):
    return num<0

def multiply(n1, n2, n3=1):
    return n1*n2*n3

def check(num):
    return num > 0 and num != 4

#lambda

homepage = lambda name, bank : f"Hey {name}, Happy {bank} Banking"
print(homepage("lisa", "sbi"))

isNegative = lambda num: num<0
print(isNegative(10))

multiply = lambda n1,n2,n3=1 : n1*n2*n3
print(multiply(2,5,8))

check = lambda num : num > 0 and num != 4
print(check(6))
