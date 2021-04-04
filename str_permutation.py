# Find all permutations of a given string

# permutate abc, “”
# 	permutate bc, a
# 		permutate c, ab
# 			permutate “”, abc
# 			print “abc” <——— OUTPUT

# permutate abc, “”
# 	permutate bc, a
# 		permutate b, ac
# 			permutate “”, acb
# 			print “acb” <——— OUTPUT


# permutate abc, “”
# 	permutate ac, b
# 		permutate c, ba
# 			permutate “”, bac
# 			print “bac” <——— OUTPUT


# permutate abc, “”
# 	permutate ac, b
# 		permutate a, bc
# 			permutate “”, bca
# 			print “bca” <——— OUTPUT


# permutate abc, “”
# 	permutate ab, c
# 		permutate b, ca
# 			permutate “”, cab
# 			print “cab” <——— OUTPUT

def permutation(str):
    permutate(str, '')
    print()
    permutate_swap(list(str))

def permutate(str, prefix):
    if str == '':
        print(prefix)
    else:
        for i in range(len(str)):
            permutate(str[0:i] + str[i+1:], prefix+str[i])

def permutate_swap(str, result=''):
    if (str == []):
        print(result)
    else:
        for i in range(len(str)):
            str[0], str[i] = str[i], str[0]
            permutate_swap(str[1:], result + str[0])
            str[i], str[0] = str[0], str[i]

permutation("abc")