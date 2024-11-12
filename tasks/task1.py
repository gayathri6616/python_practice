word = "   this  is    python   class day 3  "

"""
Expected Output: 
--------------------
This-is-pYthon-class-daY-3
"""

#word = word.lstrip()
#word = word.rstrip()
word = word.split()
word = "-".join(word)
word = word.capitalize()
word = word.replace("y","Y")
print(word)
