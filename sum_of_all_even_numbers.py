# A program that takes a list of numbers as input and returns
#the sum of all even numbers in the list
number = []
e_num = []

numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
numb = int(numb)

while numb > 0:
    number.append(numb)
    numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
    numb = int(numb)

for num in number:
    if num % 2 == 1:
        e_num.append(num)
        
e_total = sum(e_num)

