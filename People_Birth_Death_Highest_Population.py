# Listen!
# Big enough example
# Brute Force
# Optimize - BUD (Bottlenecks, Unnecessary, Duplicative), space-time tradeoffs
# Wakthrough - Walk through the approach in detail before coding
# Implement - write beautiful code and refactor it to clean up unnecessary things
#   * Use good variables
#   * Modularize
# Test - First analyze, then use test cases (small tests, edge cases, big
#     tests). Test code and not algorithm. Provide different inputs and
#     walkthrough the code

# question: given a list of people with their birth and death years, find the
# years with the highest population

# questions:
# 1. Are any of them alive?
# 2. How is the input given? An array of ht etc?
# 3. Do you want to return both the year and the max value or just the max value?

# Example - have a big enough sample case and make it variety
# 1985-2020
# 1984-2001
# 1927-1983
# 1908-1984
# 1978-2009
# 1934-1967
# 980-1290  
# 2000-2090
# 2000-2009

# Highest population years
# 1927-1983: 2
# 1984: 2
# 1985-2001: 2

# BRUTE FORCE 
# Algorithm - O(p) * O(y) + O(k)
# For each person p:
#   For y in p's birth-death:
#       if y in hash_table:
#           hash_table[y]++
#       else:
#           hash_table[y] = 1
# v = max(hash_table.values())
# for k in hash_table:
#   if hash_table[k] == v:
#       print(k,v)

list_of_births_deaths = [[1985,2000], [1908, 1991], [1971, 2009], [1956, 2003], [1965, 1985], [1978, 2019], [2000, 2020]]
population_ht = {}

def populate_population_counts():
    for person in list_of_births_deaths:
        for year in range(person[0], person[1] + 1):
            if year in population_ht:
                population_ht[year] = population_ht[year] + 1
            else:
                population_ht[year] = 1

def list_all_years_max_population():
    max_population = max(population_ht.values())
    for year in population_ht:
        if population_ht[year] == max_population:
            print(year, max_population)

if __name__ == "__main__":
    populate_population_counts()
    list_all_years_max_population()


# BRUTE FORCE 
# Algorithm - O(PY + P) = O(PY)
# For year in min(birth)-max(death):
#   ht[year] = 0
#   for p in person:
#       if p.birth >= year and p.death <= year
#           ht[year]++

full_list_input = []
population_ht = {}
# O(I) - I is #of people
for i in list_of_births_deaths:
    full_list_input = full_list_input + i

# O(P) - for min where P is a list of all birth, death years
# O(P) - for max where P is a list of all birth, death years
# O(Y*I) - for min-max we go through each person
for year in range(min(full_list_input), max(full_list_input) + 1):
    population_ht[year] = 0
    for p in list_of_births_deaths:
        if p[0] <= year and p[1] >= year:
            population_ht[year] = population_ht[year] + 1
# O(P)
print(max(population_ht.values()))

# Optimized 1
# Algorithm - O(I^2)
# loop i through all people
#   loop j through all people
#        if j.birth <= i.birth and j.death >= i.birth
#           ht[i.birth]++
#           max_year = max(max_year, ht[i.birth])

# O(U*P) where U is unique years and P is the population
populate_ht = {}
max_year = 0
for years in list_of_births_deaths:
    birth = years[0]
    if birth not in populate_ht:
        populate_ht[birth] = 0
    for seq_years in list_of_births_deaths:
        seq_birth = seq_years[0]
        seq_death = seq_years[1]
        if birth >= seq_birth and birth <= seq_death:
            populate_ht[birth] = populate_ht[birth] + 1
            max_year = max(max_year, populate_ht[birth])

print(max_year)


# Optimized 2
# Example
# 1998-2020
# 1885-1985
# 1909-1985
# 1986-2020
# 1885-1909
# 1765-1871

# What really matter is that when there's a birth population goes up and when
# there's a death population goes down. So we can order this on a line with one
# end starting at min(birth) and the one ending at max(birth)

# |--------------------------------------------|
# min(birth)                                max(birth)
# 1765(b)  1871(d)  1885(b*2)   1909(1b1d)      2020
#   1       -1         2        1 -1

# Array
# [0-(2020-1765)]
# 0-1765
# 1-1766
# ..
# x-1871 (1871-1765 = 106)

# Algorithm
# Get min and max birth years - O(P)
# Create an array that holds maxbirth-minbirth
# Loop through each person:
#       Increase person's birth index count by 1
#       Decrease person's death index count by 1 (assume the person's death year, the person is still alive. It's the year after we should consider the person dead)
# Loop through the array
#   keep a running total and a maxyear/pop and return it

def get_highest_population_year(people): # O(P) + O(P) + O(P) + O(P) + O(Y) = O(P+Y)
    min_birth, max_birth = get_min_max_birth(people) # O(P) + O(P) + O(P)
    delta_array = populate_delta_counts(people, min_birth, max_birth) # O(P)
    max_year_population = calculate_running_total_max(delta_array, min_birth) # O(Y)
    return max_year_population

def get_min_max_birth(people): # O(P) + O(P) + O(P)
    birth_list = list(map(lambda x: x['Birth'], people))
    return min(birth_list), max(birth_list)

def populate_delta_counts(people, min_birth, max_birth): # O(P)
    delta_array = [0] * (max_birth - min_birth + 1) # O(P)
    for person in people: # O(P)
        delta_array[person['Birth'] - min_birth] = delta_array[person['Birth'] - min_birth] + 1
        if (person['Death'] < max_birth):
            delta_array[person['Death'] - min_birth + 1] = delta_array[person['Death'] - min_birth + 1] - 1
    return delta_array

def calculate_running_total_max(delta_array, min_birth):
    running_sum = 0
    max_year = 0
    max_population = 0
    for year_idx, year_count in enumerate(delta_array): # O(Y)
        running_sum = running_sum + year_count
        if (running_sum > max_population):
            max_population = running_sum
            max_year = year_idx + min_birth
    return (max_year, max_population)

people = [
    { "Birth": 1998, "Death": 2020 },
    { "Birth": 1885, "Death": 1985 },
    { "Birth": 1909, "Death": 1985 },
    { "Birth": 1986, "Death": 2020 },
    { "Birth": 1885, "Death": 1909 },
    { "Birth": 1765, "Death": 1871 }
]

people = [
    { "Birth": 1985, "Death": 2000 },
    { "Birth": 1908, "Death": 1991 },
    { "Birth": 1971, "Death": 2009 },
    { "Birth": 1956, "Death": 2003 },
    { "Birth": 1965, "Death": 1985 },
    { "Birth": 1978, "Death": 2019 },
    { "Birth": 2000, "Death": 2020 }
]

people = [
    { "Birth": 1985, "Death": 1991 },
    { "Birth": 1986, "Death": 1986 }
]

print(get_highest_population_year(people))