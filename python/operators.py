#Arithmetic --> +, -, *, %, /, //, **
a= 1+2
print(a)
print("================================================")

a = 1 - 5
print(a) 
print("================================================")

a = 5 * 5
print(a)
print("================================================")

a = 3 % 5
print(a)
print("================================================")

a = 14 % 3
print(a)
print("================================================")

a = 8 / 8
print(a)
print("================================================")

a = 5 / 2
print(a)
print("================================================")

a = 5 // 2
print(a)
print("================================================")

a = 5 ** 3
print(a)
print("================================================")
 
# relational --> <, >, ==, !=, <=, >=

a = int(input("Enter the num: "))
if (a>0):
    print(f"{a}, a is great than zero")
    if(a==1):
        print("This is one")
    elif(a<=50):
        print(f"{a},a is less than 50")
    elif(a>=50):
        print(f"{a},a is great than 50")
    else:
        print("This is != Zero")
else:
    print(f"{a},This is less than zero ")
print("================================================")

a = [1,2,3]
b= [3,4,5]
print(a > b)
# logical --> and, or 
num = 50
print(num<100 and num%2==0)
print(num<100 or num%2!=0)
print("================================================")

# short-hand assignment --> +=, -=, *=, %=, /=, //=,
x = 10
x += 5
print(x)
print("================================================")

# membership --> in, not in
print('anil' in 'anilkumar')
print('sri' not in 'anilkumar')
print('Anil' in 'anilkumar')
print("================================================")

# identify --> is, is not
a = "code"
b = "code"
print(id(a))
print(id(b))
print(a==b)
print(a is b)
print("================================================")

c = ["code"]
d = ["code"]
print(id(c))
print(id(d))
print(c == d)
print (c is d)
print("================================================")

a = 257
b = 257
# object pooling range (-6, +256)
print(a==b)
print(a is b)


