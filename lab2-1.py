# Author: ATN 12/1/21

def sum_all(a):
    '''Returns all the numbers leading up to and including the one
    specified by the user.'''
    total = 0
    for x in range(int(a + 1)):
        total += x
    return total


choice = int(input("Please choose a number: "))
print(sum_all(choice))
