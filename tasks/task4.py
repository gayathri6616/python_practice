""" 
TASK: Take email as an input from user, than can contain 
      lower, upper, numbers and domains like @gmail.com, @hotmail.com, @yahoo.com
    After separating the domain,
      print the domainless lowercase name and count the number of vowels in the email.

      Your code should work for all the mails, irrespective of the domain.
      NOTE: No invalid email should be taken

Sample Input1:
  NIck@gmail.com
Sample Output1:
  nick ---- 1

Sample Input2:
  coDEwala@yahoo.com
Sample Output2:
  codewala ---- 4

Sample Input3:
  SteeveRogers123@hotmail.com
Sample Output3:
  steeverogers123 ---- 5

"""
user = input("enter the email :")
name = user[:user.find('@')]
name = name.lower()
vowel = "aeiou"
# v1 = name.count('a') + name.count('e') + name.count('i') + name.count('o') + name.count('u')
# print(f'{name} ------- {v1}')

count = 0
for i in name:
    #print(i)
    if i in vowel:
        print(i)
        count += 1
print(count)            
