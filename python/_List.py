'''list allows duplicate values
it is heterogeous, ordered, mutuable
List --> []'''

_list = ['gayathri',1,2,2.5,True,2,2,' ',]
print(_list)
print('=================================')

# index
# syntax:  list.index(element, start, end)
list1 = [10,20,30,40,20,30]
print(list1.index(20))
print(list1.index(30,3))
#print(list1.index(50)) #element not found --> ValueError
print('=================================')

# slicing
# syntax: list[start:stop:step]
print(list1[:])
print(list1[1])
print(list1[:6:2])
print(list1[::-1])
print(list1[-5:])
print(list1[-5:-1])
print(list1[-5:-2:2])
print(list1[-1:])
print('=================================')

print('in') 
print(20 in list1)
print(50 in list1)
print('=================================')

# not in 
print(20 not in list1)
print(50 not in list1)
print('=================================')

# len 
print(len(list1))
print('=================================')

# count
print(list1.count(20))
print('=================================')

# modify list
list2 = [10,20,30,40] 
list2[2]= 35
#list2[4] = 25 # index out of range --> indexerror
print(list2)
print('=================================')

# insert --> position , value
_list = [1,2,3,4,5]
_list.insert(2,7)
_list.insert(10,6)
print(_list)
print('=================================')

# append --> added single element to the end , one element only allowed
print("===== append ========")
list3 = [12,13,14,15,16]
list3.append(20)
list3.append([11,22,33])
print(list3)
print('============= end ==================')

# extends --> another list added to the end , more than one element
list4 = [77,88,99,33]
list4.extend([66,55,33])
print(list4)
print('=================================')

# pop --> removed last element and declare position value (indexvalue)
list4.pop()
list4.pop(3)
#list4.pop(6) --> indexerror
print(list4)
print('=================================')


# remove --> value 
'''empty --> TypeError
not found value --> ValueError'''
list5 = [30,40,50,60,70]
list5.remove(30) 
print(list5)
print('=================================')

# clear --> values only removed , variable will be ,it's displays empty list
list6 = [11,22,33,44,55]
list6.clear()
print(list6)
print('=================================')

# del
# list7 = [12,23,34,45,56]
# del list7[3]
# # del list7[5] --> indexerror
# del list7[]
# print(list7)

# modify
list8 = ['a','e','f']
list8[1:4] = ['b','c','d']
print(list8)
print('=================================')

# concatenation --> +
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2  
print(list3) 
print('=================================')

# multiply lists with scalar
list1 = list1 * 3
print(list1)
list2 = list2 * 0
print(list2)
list3 = list3 * -1
print(list3)
print('=================================')

# min, max, sum, reverse
list9 = [12,2,34,8,78,9]
print(min(list9))
print(max(list9))
print(sum(list9))
list9.reverse()
print(list9)
print('=================================')

# slicing 
list3 = [12, 13, 14, 15, 16, 20, [11, 22, 33]]
print(list3[-1][2])
print('=================================')

# sort
list10 = ['gaya','Anil','sri','VIhya','AKKI']
list10.sort() # asc
print(list10) 
list10.sort(reverse=True) #desc
print(list10)
list10 = sorted(list10)
print(list10)
print('=================================')

# enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
print('=================================')

# list conversion
data = {1:'A',2:'b',3:'c'}
data = list(data.items())
print(data)
print("==============================")

# unpacking
bio = ["1001", "steeve", "brooklyn"]
_id, *rest = bio
print(f"Remaining elements after unpacking bio: {rest}")
print("==============================")

# list comparsion
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
print(f"[{arr1} == {arr2}] -> {arr1 == arr2}")  # --> True
print(f"[{arr1} is {arr2}] -> {arr1 is arr2}")  # --> False (because it will compare id's)

# copy
nums1 = [1, 2, 3, 4]
nums2 = nums1 #it is not copying the list, just referencing
nums2.append(5)
print(f"nums1 after appending 5 through nums2: {nums1}")

nums3 = nums1.copy() #it is copying the list
nums3.append(6)
print(f"nums1 after appending 6 to a copy: {nums1}")

# nested list
arr = [[1, "steeve", 40000], [2, "tony", 30000, [3, "pepper", 10000]]]
print(f"The salary of {arr[1][3][1]} is {arr[1][3][2]}.")


 