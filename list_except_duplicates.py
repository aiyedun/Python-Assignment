#Write a function that take list of numbers and return a new list
#that contains all the numbers in the input list except duplicates

def list_except_duplicates(A):
    n_num = []
    for element in A:
        if element not in n_num:
            n_num.append(element)
        else:
            continue
    n_num.sort()
    return n_num

##number = []
##numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
##numb = int(numb)
##while numb > 0:
##    number.append(numb)
##    numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
##    numb = int(numb)
##
##n_num = []
##for element in number:
##    if element not in n_num:
##        n_num.append(element)
##    else:
##        continue
##n_num.sort()
##print(n_num)

