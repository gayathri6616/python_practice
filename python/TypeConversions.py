# integer --> string

num = 505
num = str(num)
print(f"int --> str = {num} --> {type(num)}")
print("================================================")

# integer --> float
num = 505
num = float(num)
print(f"int --> float = {num} --> {type(num)}")
print("================================================")

# float --> integer
num = 505.10
num = int(num)
print(f"float --> int = {num} --> {type(num)}")
print("================================================")

# float --> string

num = 505.10
num = str(num)
print(f"float --> str = {num} --> {type(num)}")
print("================================================")

# string --> int
 
num = '505'
num = int(num)
print(f"str --> int = {num} --> {type(num)}")
print("================================================")

#name = "gaya3"
#name = int(name) or float(name)
#print(name) 
# int will give error --> valueError othen integer / float
print("================================================")

num = "505.12"
num = float(num)
num = int(num)
print(num)
print(type(num))

# in float string value
''' first convert into float
 after convert into int'''
print("================================================")

# string --> float

num = "505.11"
num = float(num)
print(num)
print(type(num))
print("================================================")

num = "505"
num = int(num)
num = float(num)
print(num)
print(type(num))
print("================================================")
# bool
# non-zeroes or non-empty -------> True
# zeroes or empty -------> False
variable = "string"
variable = bool(variable)
print(variable)

variable = "10"
variable = bool(variable)
print(variable)

variable = "20.8"
variable = bool(variable)
print(variable)

variable = ""
variable = bool(variable)
print(variable)

variable = " "
variable = bool(variable)
print(variable)

variable = "0"
variable = bool(variable)
print(variable)

variable = "-1"
variable = bool(variable)
print(variable)
print("=============== bool =======================")

#composite type conversions
# list --> tuple
name = ["gaya3","Anil","sri","vidhya",1,2,2,3]
name = tuple(name)
print(name)

# list --> set
name = set(name)
print(name)

# list --> dict
name = [['name','gaya3'],['course','cse']]
name = dict(name)
print(name)
print("================== list ==============================")

# tuple --> list
name = ("gaya3","Anil","sri","vidhya",1,2,2,3)
name = list(name)
print(name)

# tuple --> set
name = ("gaya3","Anil","sri","vidhya",1,2,2,3)
name = set(name)
print(name)

# tuple --> dict
name = ({'name','gaya3'},['course','cse'])
name = dict(name)
print(name)
print("==================== tuple ============================")

# set --> list
name = {"gaya3","Anil","sri","vidhya",1,2,3}
name = list(name)
print(name)

# set --> tuple
name = {"gaya3","Anil","sri","vidhya",1,2,2,2,3}
name = tuple(name)
print(name)
print("====================== set ==========================")


# dict --> list
name = {'name':'gaya3','course':'cse'}
name = list(name.items())
print(name)
print("==================== dict ============================")

# memory model
""" 
mutable ---> changeble & before and after changes, address should be same
immutable ---> unchangeble & before and after changes, address may be change
"""


name = "python"
print(f"Address Before Changes: {id(name)}")

name += "crt"
print(f"Address After Changes: {id(name)}")

