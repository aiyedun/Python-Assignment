# create A program that takes a list of numbers as input and returns
#the smallest number that is graeter than the average of
#all numbers in the list

numbers = []
g_av = []
average = 0

numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
numb = int(numb)

while numb > 0:
    numbers.append(numb)
    numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
    numb = int(numb)

#number.sort()
average = sum(numbers)/len(numbers)
for number in numbers:
    if number > average:
        g_av.append(number)
g_av.sort()
try:
    print(g_av[0])
except:
    print("The average of the list is graeter than all the numbers")
    



