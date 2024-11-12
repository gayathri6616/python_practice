""" 
Take a sentence and separate the vowels and consonants.
Do not convert the sentence into lower.
If the sentence contains 0 in it, consider it as invalid,
    you dont have to separate vowels & consonants

Sample Input1:
  This Is codewala
Sample Output1:
  [vowels] --- iIoeaa
  [consonants] --- Thsscdwl

Sample Input2:
  This Is DSA
Sample Output2:
  [vowels] --- iIA
  [consonants] --- ThssDS

Sample Input3:
  I Could Do This All day
Sample Output3:
  [vowels] --- IouoiAa
  [consonants] --- CldDThslldy

CONSTRAINTS:
  should not take special characters and numbers
  sentence can have spaces
  output should not contain spaces
"""
sentence = input("enter the sentence:")
vowel =" aeiou"
for i in range(0,len(sentence)):
    if (sentence[i]=='a'):
        print("--")