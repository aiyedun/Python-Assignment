# A program that takes a list of numbers as input and returns
#the list of all prime numbers in the input list
number = []
prime_num = []

numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
numb = int(numb)

while numb > 0:
    number.append(numb)
    numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
    numb = int(numb)

for num in number:
    r = 0
    for i in range(1,num):
        if num % i == 0:
            r += 1
    if r == 1:
        prime_num.append(num)
        
print(prime_num)

