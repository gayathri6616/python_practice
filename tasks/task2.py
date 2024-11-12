# Task1
"""
Task: Format and Analyze a Sentence
Description: Given a sentence, perform the following operations:

- Convert the entire sentence to uppercase.
- Count the number of occurrences of the letter 'E'.
- Replace all occurrences of the word "bad" with "good".
- Capitalize the first letter of each word.
- Find the length of the modified sentence.
- Extract a substring from the modified sentence, Get the first 10 characters.

Sample Input:
-------------
sentence = "This is a bad example of a bad situation."

Sample Output:
--------------
Uppercase: THIS IS A BAD EXAMPLE OF A BAD SITUATION.
Occurrences of 'E': 3
Replaced: This is a good example of a good situation.
Capitalized: This Is A Good Example Of A Good Situation.
Length: 42
Sliced Substring: This is a 
"""

sentence = "This is a bad example of a bad situation."
sentence = sentence.upper()
print(f'Uppercase: {sentence}')
sentence = sentence.count('E')
print(f"Occurrences of 'E' : {sentence}")
sentence = "This is a bad example of a bad situation."
sentence = sentence.replace('bad','good')
print(f'Replaced : {sentence}')
sentence = sentence.capitalize()
print(f'Capitalized : {sentence}')
sentence = sentence.title()
print(sentence)
print(len(sentence))
print(sentence[:9])
words = ["your", "text", "here"]
capitalized_words = [word.capitalize() for word in words]
print(capitalized_words)


