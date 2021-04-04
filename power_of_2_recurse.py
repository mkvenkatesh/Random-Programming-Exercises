# print all the powers of 2 between 1 and n inclusive using recursion

def power_of_2(n):
    if n == 0:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = power_of_2(n/2)
        print(2 * prev)
        return 2 * prev


power_of_2(8)