'''dict ---> {}, unordered, mutable 
key --> union, values --> allow duplicate
--> cannot use mutable data types as key in dictionary
--> keys can be any data types
--> duplicates are not allowed'''

# Type Constraints for Keys & Values
'''keys must be immutable types like strings, numbers, or tuples.
 Values can be any data type.'''

my_dict = {"name" : "gayathri", 1000 : 'id', (2, 3): "anil"}
#my_dict = {"name" : "gayathri", 1000 : 'id', [2, 3]: "anil"}
#my_dict = {"name" : "gayathri", 1000 : 'id', {2, 3}: "anil"}
#my_dict = {"name" : "gayathri", 1000 : 'id', {2:1, 3:2}: "anil"}
print(my_dict)

dictionary = {}
dictionary['id'] = "9L" # modify
dictionary.update({"name" : "gayathri" , "age" : 20})
dictionary.update(name = 'anil' , age = 23) # update 
print(dictionary)

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(dictionary.get('name1'))
dictionary.pop('id')
print(dictionary)

print('name' in dictionary)
print(23 in dictionary.values())
















