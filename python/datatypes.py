print()#print function is used to display output
input()#input() function is used to display user input
name=input("enter the name: ") # string input will allow
print(name)

""" datatypes are two types
1. primitive --> int, string, float, boolen
2. composite or primitive --> list, tuple, set, dict, frozenset """
name=int(input("enter the number: "))
#int funct allow only integer number
print(name)
print("================================================")

Name = float(input("enter the num: "))
#float funct allow only float or integer number = 25.5 and 10
print(Name)
print("================================================")

#composite declaration
_list = [1,2,2,3,4]
print(_list)
# empty list
list1 = []
print(list1)
print("================================================")

# Tuple
_tuple=(2,3)
print(_tuple)
#empty tuple
tuple1 =()
print(tuple1)
print("================================================")

# set
_set = {"name",1,2}
print(_set)
#empty set
var = set()
print(var)
print("================================================")

#dict 
dict1= {'name':'gaya3','roll':5}
print(dict1)
#empty dict
dict1 = {}
# string - formatting
# f string
myname = input("enter the name: ")
print(f"hello {myname},\n All the the best")



