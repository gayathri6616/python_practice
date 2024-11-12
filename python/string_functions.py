word = 'python training'
print(len(word))
word = word.upper()
word = word.lower()
word = word.capitalize()
word = word.replace(" ",'-')
word = word.count('n')
print(word)
word1 ="    This is the python training   "
word1 = word1.lstrip() #left side starting spaces
word1 = word1.rstrip() # right side ending spaces 
word1 = word1.strip() # both left and right sides spaces
#word1 = word1.index('i') #value is not found ,it will give error
#word1 = word1.find('i') # value is not found, it will not give any error
word1 = word1.rfind('i') # from right side first "i" index value
print(word1)
word1 ="    This is the python training   "
word1 = word1.split()
word1 ='-'.join(word1)
print(word1)




