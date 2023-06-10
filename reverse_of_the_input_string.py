#Create a program that takes a string as input,
#and returns a new string that is the reverse of the input string

word = input("Enter any word of your choice: ")
word = list(word.lower())
new_word = word[::-1]
space = ""
new_word = space.join(new_word)
print(new_word)

