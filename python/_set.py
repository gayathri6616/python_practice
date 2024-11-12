# set ---> {}, set(), unordered, mutable
# ---> it does not allow duplicate

# set
s = {1,2,3,2,1}
print(s)
print("=======================")

# add
s.add(4)
print(s)
print("=======================")

# remove --> Raises a KeyError if the element is not found.
s.remove(2)
print(s)
print("=======================")

# discard --> element is not found, no error.
s.discard(5)
print(s)
print("=======================")

# pop --> set is empty, raises a KeyError.
s = {1, 2, 3}
element = s.pop()
print(element)  
print(s)  
print("=======================")

# update 
s = {1, 2, 3}
s.update([4, 5, 6, 7])
print(s) 
print("=======================")


# union
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.union(s2)
print(result) 
print("=======================")

#intersection
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.intersection(s2)
print(result)  
print("=======================")

# difference
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s2.difference(s1)
print(result)  
print("=======================")

# isdisjoint
s1 = {1, 2, 3, 5}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))
print("=======================")

# issubset and superset
s1 = {1, 2,}
s2 = {1, 2, 3}
print(s1.issubset(s2))
print(s1.issuperset(s2)) 
