# Listen
# Big enough example
# Brute force approach first if possible and then proceed with optimization
# Algorithm Optimization (BUD)
#   1. BUD - Bottlenecks, Unnecessary Work, Duplicated Work
#   2. Look for space-time tradeoffs

# Find all solutions for a^3 + b^3 = c^3 + d^3 (for all 1<=a, b, c, d <=1000)

#  a=b=c=d=1 => 1+1 = 1+1
#  a=2 b=c=d=1 => 8+1 = 1+1
#  a=1000 b=2 c=d=1 => 1000^3 + 8 = 1+1

# brute force O(N^4)
# for a in 1..1000:
#   for b in 1..1000:
#       for c in 1..1000:
#           for d in 1..1000:
#               if a**3 + b**3 == c**3 + d**3:
#                   print(a,b,c,d)

# for a in range(1, 1001):
#     for b in range(1, 1001):
#         for c in range(1, 1001):
#             for d in range(1, 1001):
#                 if a**3 + b**3  == c**3 + d**3:
#                     print (a,b,c,d)

# optimization 1 - if ((a==c and b==d) or (a==d and b==c), don't cube it - still O(N^4)
# for a in range(1, 1001):
#     for b in range(1, 1001):
#         for c in range(1, 1001):
#             for d in range(1, 1001):
#                 if ((a==c and b==d) or (a==d and b==c)):
#                     print (a,b,c,d)
#                 elif a**3 + b**3  == c**3 + d**3:
#                     print (a,b,c,d) 

# optimization 2 - given a, b, c, you can solve for D - O(N^3)
# for a in range(1, 1001):
#     for b in range(1, 1001):
#         for c in range(1, 1001):
#             d = int(((a**3 + b**3 - c**3) ** (1./3.)).real)
#             if (a**3 + b**3 == c**3 + d**3):
#                 print (a,b,c,d)

# optimization 3 - don't duplicate the work of calculating c,d pairs for a given
# (a,b) pair. Use a hash table to store all the (c,d) cube sum and the pairs
# that go with it and use that for lookup against (a,b) cube sum
# O(N^2)
# ht_cd_pair = {}
# for c in range(1, 1001):
#     for d in range(1,1001):
#         result = c**3+d**3
#         if result not in ht_cd_pair:
#             ht_cd_pair[result] = [(c,d)]
#         else:
#             ht_cd_pair[result].append((c,d))

# for a in range(1,1001):
#     for b in range(1,1001):
#         result = a**3 + b**3
#         if result in ht_cd_pair:
#             for i in ht_cd_pair[result]:                
#                 print (a,b,i[0],i[1])


# optimization 4 - you already generated the hash table with cd pairs, leverage
# that for (a,b) as well
ht_cd_pair = {}
for c in range(1, 1001):
    for d in range(1,1001):
        result = c**3+d**3
        if result not in ht_cd_pair:
            ht_cd_pair[result] = [(c,d)]
        else:
            ht_cd_pair[result].append((c,d))

for key, value in ht_cd_pair.items():
    for pair1 in value:
        for pair2 in value:
            print (pair1, pair2)