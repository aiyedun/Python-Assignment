#Create a program that takes a string aas input,
#and returns the most common character in the string

word = input("Enter any word of your choice preferable with multiple identical letters: ")
word = list(word.lower())
count = dict()

for char in word:
    if char not in count:
        count[char] = 1
    else:
        count[char] +=1
lst = list()
for k,v in list(count.items()):
    lst.append((v,k))
lst.sort()
print(lst[-1])

