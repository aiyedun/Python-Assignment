#Write a function that takes two sorted list and return a new sorted list
#that contains all the element fom both list in ascending order

def two_list_in_ascending_order(A,B):
    A.sort()
    B.sort()
    c_num = []
    for element in A:
        c_num.append(element)
    for element in B:
        c_num.append(element)
    c_num.sort()

    return c_num

##number1 = []
##numb1 = input("Enter any number of your choice and enter zero(0) to end the sequence1: ")
##numb1 = int(numb1)
##while numb1 > 0:
##    number1.append(numb1)
##    numb1 = input("Enter any number of your choice and enter zero(0) to end the sequence1: ")
##    numb1 = int(numb1)
##number1.sort()
##
##
##number2 = []
##numb2 = input("Enter any number of your choice and enter zero(0) to end the sequence2: ")
##numb2 = int(numb2)
##while numb2 > 0:
##    number2.append(numb2)
##    numb2 = input("Enter any number of your choice and enter zero(0) to end the sequence2: ")
##    numb2 = int(numb2)
##number2.sort()
##
##c_num = []
##for element in number1:
##    c_num.append(element)
##for element in number2:
##    c_num.append(element)
##c_num.sort()
##
##print(c_num)
