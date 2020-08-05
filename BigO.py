N = 3

# The loop executes N times so Big O is O(N)
print ("Print 0 to N")
for i in range(N):
    print (i)

# The outer loop runs N times and the inner loop runs N times for each outer
# loop, so O(N) * O(N) = O(N^2) 
print ("\nPrint pairs")
for i in range(N):
    for j in range(N):
        print (i, j)

# The loop still has to run for N times, even though printing happens only for
# half the time, so it's O(N)
print ("\nPrint evens")
for i in range(N):
    if (i % 2 == 0):
        print (i)

# First loop runs N times and second loop runs N times so it's N+N but we don't
# call it O(2N). In Big O, we drop the constants. All we care about is that the
# code scales linearly to a given input. So the Big O for this code is O(N)
print ("\nPrint evens and odds")
for i in range(N):
    if (i % 2 == 0):
        print (i)
for i in range(N):
    if (i % 2 != 0):
        print (i)

# Outer loop runs N times and inner loop runs N-i times, so it's N*(N-I) =
# O(N^2)
print ("\nPrint ordered pairs")
for i in range(N): 
    for j in range (i, N):
        print ("{},{}".format(i, j))

# This one is tricky. This looks like O(N^2) but it's really not. When we say
# O(N) for an algorithm, it's O(N) for when N is some particular thing. It's not
# inherently O(N). So for the above code we should really say O(N * M), since A
# and B are not guaranteed to have the same length, unless you were told that A
# & B are the same length
print ("\nPrint ordered pairs with variable strings")
for i in "int":
    for j in "rules":
        print ("{}, {}".format(i, j))


# int last_death = Integer.Min
# # Step 1: get last death -  O(P), where P are the number of people
# for (Person person: people) {
#     last_death = Max(last_death, people.death)
# }
# # Step 2: increment counter for each year someone is alive - O(P) * O(L) = O(P*L), where L is max life span
# int[] counter = new int[last_death]
# for (Person person: people) {
#     for (int year = person.birth; year < person.death; year ++) {
#         counter[year]++
#     }
# }
# # Step 3: find population peak - O(Y), where Y is total # years
# int highest_population = 0
# for (int year = 0; year < counter.length; year ++) {
# 			highest_population = max(highest_population, counter[year])
# }

class Person:
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death

    def __str__(self):
        return f"This person was born in {self.birth} and died on {self.death}"

p1 = Person(1985, 2020)
p2 = Person(1971, 2008)
p3 = Person(1986, 2019)
p4 = Person(1954, 1990)

listOfPeople = [p1, p2, p3, p4]
last_death = 0

 # Step 1: get last death - O(P)
for p in listOfPeople:
    last_death = max(last_death, p.death) # max is constant time function so doesn't matter for O

print(last_death)

# Step 2: increment counter for each year someone is alive - O(P) * O(L) = O(P*L), where L is max life span
counter = {}
for p in listOfPeople:
    for year in range(p.birth, p.death):
        if str(year) not in counter:
            counter[str(year)] = 0
        counter[str(year)] = counter[str(year)] + 1

print(counter)

# Step 3: find population peak - O(Y), where Y is total # years
highest_population = 0
for key in counter.keys():
    highest_population = max(highest_population, counter[key])

print (highest_population)

# Total O = O(P) + O(P*L) + O(Y) = O(P*L) + O(Y)