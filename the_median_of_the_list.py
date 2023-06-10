# A program that takes a list of integers as input and returns
#the median of the list
def median_of_the_list(A):
    A.sort()
    if len(A) % 2 == 0:
        mid = A[(len(A)//2-1):(len(A)//2+1)]
        median = sum(mid)/2
    else:
        mid = A[(len(A)//2)]
        median = mid
    return median

##number = []
##mid = []
##median = 0
##
##numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
##numb = int(numb)
##
##while numb > 0:
##    number.append(numb)
##    numb = input("Enter any number of your choice and enter zero(0) to end the sequence: ")
##    numb = int(numb)
##
##number.sort()
##if len(number) % 2 == 0:
##    mid = number[(len(number)//2-1):(len(number)//2+1)]
##    median = sum(mid)/2
##else:
##    mid = number[(len(number)//2)]
##    median = mid
##print(median)

