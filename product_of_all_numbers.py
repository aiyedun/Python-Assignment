# A program that takes a list of numbers as input and returns
#the product of all integers in the list

def product_of_all_integers(A):
    p_num =1
    for num in A:
        p_num *= num 
        
    return p_num

##number = []
##p_num =1
##
##numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
##numb = int(numb)
##
##while numb > 0:
##    number.append(numb)
##    numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
##    numb = int(numb)
##
##for num in number:
##    p_num *= num 
##        
##print(p_num)

