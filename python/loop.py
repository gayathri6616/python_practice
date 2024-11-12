"""
control structures
looping ----> for, while, for-else, while-else
conditional ---> if, else, nested if-else
unconditional ---> pass, break, continue
"""
# for loop
for i in range(10,0,-2): # start, stop, step value
    print(i)

'''string length and range length must be equal or less than length of sting,
if greater than string it gives 
index error --> string index out of range '''

name = "gayathri"  
for n in range(0,8): # we can declara anything "n" place
    print(name,n) # it print name 8times
    #print(name[n]) # it print character by character 

name = input('enter:')
for n in range (5):
    name = input('enter:')
    print(name)

for i in range(5):
    data = int(input("Enter Number: "))
    if data < 0:
        print("Negatives Entered, Terminating Entire Loop")
        break
else:
    print("No Negative values Entered")

# while
tata = "goodbye"
current = 0
while current < len(tata):
    print(tata[current])
    current +=1

tata = "goodbye"
current = len(tata) - 1
while current >= 0:
    print(tata[current])
    current -= 1
# while else
start = 0
while start < 5:
    data = int(input("Enter Number: "))
    if data < 0:
        print("Negatives Entered, Terminating Entire Loop")
        break
    start += 1
else:
    print("No Negative values Entered")

