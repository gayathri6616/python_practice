# representation --> 4 
a = "Gayathri"
b = 'Anil'
c = '''anil is my thammuddu'''
d = """i am his akka"""

print("=====indexing --> 2 Positive and negative======")
print(f"positive indexing {a[5]}")
print(f"negative indexing {b[-2]}")
print(f"{a[5]}{b[-2]}")
print('====================================')

# string - formatting
print('=========f string============')
myname = input("enter the name: ")
print(f"hello {myname},\n All the the best")

print("============ quote character =============")
print('python\'s')
print('python\\\'s')

print("============ multi line sting ==============")
#using \, ''', """
sent = '''this 
            is python
                   killer'''
print(sent)
sent = "This \
is python \
killer"
print(sent)
print("=================================")

# string concatenation
name1 = "akka"
name2 = 'thambi'
relation = name1 + " & " + name2
print(relation)
print("=================================")

# unicode
telugu = "నేను తెలుగు నేర్చుకుంటున్నాను"
print(telugu[5])
korean = "나는 학생이에요"
print(korean[3])

# slicing
course = 'python training code'
""" 
syntax --> var[start:stop:step]
syntax --> var[start:stop]
"""
print('=============== positive slicing =================')
print(course[5])
print(course[0:6])
print(course[0:6:1])
print(course[0:6:2])
print(course[0:])
print(course[:6])
print(course[:])
print(course[::2])
print("================== negative slicing ====================")
print(course[-1])
print(course[-4:-1])
print(course[:-1])
print(course[-1:])
print(course[::-1])
print(course[-4:])
print(course[-4::2])

