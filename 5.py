'''
Write a Python program that takes a text file as input and returns the number of
words of a given text file.
Note: Some words can be separated by a comma with no space
'''
def words():
   with open("1.txt") as x:
       data = x.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(words())
