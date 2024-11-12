""" 
data = [[1001, "steeve", ["brooklyn", "USA", ["captain america"]]]]
extract the captain america from the data and print it in uppercase

OUTPUT:- 
  CAPTAIN AMERICA
"""
data = [[1001, "steeve", ["brooklyn", "USA", ["captain america"]]]]
print(data[-1][-1][-1][-1].upper())
print(data[0][2][2][0].upper())
data = data[0][2]
print(data[-1][-1].upper())