""" --> To re-use the code
--> syntax: 
	def functionName(parameters):
		pass
--> function will get execute, only when it's called
--> if control finds return in function, it will get out of that entire function
"""

# non-return function & parameterized function
def welcome (name, bank):
    print(f"1. name:{name},bank:{bank}")
welcome("gayathri", "canada")

# return function & parameterized function
def welcome (name, bank):
    return(f"2. name:{name},bank:{bank}")
print(welcome("anil", "sbi"))

# non-parametrized function & return function
def oneToFive():
  for i in range(1, 6):
    print(i)
  return "3.done"
print(oneToFive())

# non-parametrized function & non-return function
def oneToFive():
  for i in range(1, 6):
    print(i)
print(oneToFive())

# *args --> tuple
def numbers(a, *args):
    print(f"Numbers are {a}, {args}")
print(numbers(10, 20, 30, 40))

# **kwargs(variable keyword arguments)

"""
ORDER:
   positional, Default
  	    *args, **kwargs
"""

def details(**kwargs):
    print(kwargs)

details(age=15, name="gayathri", brother="anil")

print("--------------------------------------------")

def details(a, **kwargs):
    print(f"{a}:{kwargs}")

details(100, age=15, name="latha", brother="maaz") 

print("--------------------------------------------")

def details(a, *args, **kwargs):
    print(a, args, kwargs)
details(10,20,30,40,)
# passing parameters by unpacking
clrs = ("red", "blue", "green")

def colors(c1, c2, c3):
    print(f"Colors are {c1}, {c2}, {c3}")

colors(clrs[0], clrs[1], clrs[2])
colors(clrs[0], clrs[2], clrs[1])
colors(*clrs)