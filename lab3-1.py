# Author: ATN 12/2/21

def sum_to(n):
    total = 0
    x = 0
    while x <= n:
        total += x
        x += 1
    return total


selection = int(input("Please choose a number: "))
print(sum_to(selection))
