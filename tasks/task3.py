""" 
TASK: Get the username from the user and generate the userid
For Memory Issues, Limit the userid to length 10 with following conditions
  - if the length of userid is less than 10, then cover it with 0 at prefix
  - if length of userid exceeds 10, then remove the extra characters

For the security reasons, we had to mask the user id with following:
  replace the last two characters with 'X'
Print the userid along with masked userid

Sample Input1:
  nick
Sample Output1:
  000000nick ---- 000000niXX

Sample Input2:
  codewala
Sample Output2:
  00codewala ---- 00codewaXX

Sample Input3:
  SteeveRogers
Sample Output3:
  SteeveRoge ---- SteeveRoXX

"""
username1 = input("enter the name :")
name = ((10 - (len(username1)))*'0') +username1
print(f'{name[:8] + 'XX'}')
list1 =[1,2,3,4]
num = (list1 > 3)
print (num)

