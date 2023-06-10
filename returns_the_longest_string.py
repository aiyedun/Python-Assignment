#Write a function that take list of strings and return the longest
#sting in the list

A = input("Enter any word of your choice: ")
B = input("Enter any word of your choice: ")
C = input("Enter any word of your choice: ")
words = [A,B,C]
count = list()

for word in words:
    count.append((len(word),word))

count.sort(reverse = True)
print(count[0])
