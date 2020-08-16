"""
Suffix Arrays - Optimized O(n log n) - prefix doubling

A suffix is a non-empty substring at the end of the string. A suffix array
contains all the sorted suffixes of a string

A suffix array provides a space efficient alternative to a suffix tree which
itself is a compressed version of a trie. Suffix array can do something a suffix
tree can, with some additional information such as Longest Common Prefix (LCP)
array. 

A suffix array can be constructed from Suffix tree by doing a DFS traversal of
the suffix tree. In fact Suffix array and suffix tree both can be constructed
from each other in linear time.

Advantages of suffix arrays over suffix trees include improved space
requirements, simpler linear time construction algorithms (e.g., compared to
Ukkonen’s algorithm) and improved cache locality 

source: https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/

# Algorithm
1. The first step is to generate all the suffix starting with the whole string
   and then looping through and producing the 1 to end, 2 to end etc until the
   end character.
2. We assign current and next rank to the first two characters of the suffixes.
   A simple rank could be str[i]-'a'. If no characters are found, set it to -1
        Index    Suffix            Rank          Next Rank 
        0        banana            1              0
        1        anana             0              13    
        2        nana              13             0
        3        ana               0              13
        4        na                13             0 
        5        a                 0             -1 
3. Sort the array using the current and next rank
		Index    Suffix            Rank          Next Rank 
        5        a                 0               -1
        1        anana             0               13    
        3        ana               0               13
        0        banana            1               0
        2        nana              13              0
        4        na                13              0  
	
4. So far we sorted all the suffixes through first two characters. Now we do the
        next 4, 8 and so on until 2*len(n) times. We loop from 4 to 2N and
        calculate the current and next rank the following way.

        a. Current Rank - Assign 0 as the current rank for the first suffix. For
        remaining suffixes, we take the rank pair from previous iteration i.e
        (current rank, next rank) from the previous time and see if it's the
        same as the rank pair of the previous suffix. If they are the same, set
        current rank to same as previous suffix current rank, else increment by
        1 and set it as current rank for the current suffix.
        
            Index      Suffix          Rank       
            5          a               0     [Assign 0 to first]        
            1          anana           1     (0, 13) is different from previous
            3          ana             1     (0, 13) is same as previous     
            0          banana          2     (1, 0) is different from previous      
            2          nana            3     (13, 0) is different from previous      
            4          na              3     (13, 0) is same as previous  


        b. Next Rank - suppose k is the loop and the initial value is 4, we take
        the subarray from k/2 to end and see what current rank is assigned for
        that suffix (i.e. suffix[k/2:].current_rank) and set that rank. If no
        suffix is found or theres no characters for k/2 to end, set it to -1

            Index      Suffix          Rank        Next Rank
            5          a               0             -1
            1          anana           1              1      
            3          ana             1              0 
            0          banana          2              3
            2          nana            3              3 
            4          na              3              -1       

5. Now sort current and next rank

6. Proceed like this until k <= 2N
"""

def prefix_doubling_suffix_array(n):
    n_len = len(n)

    # base cases
    if n_len == 0:
        return []
    if n_len == 1:
        return [0]

    # declare suffixes dictionary which will hold all the suffixes in the sorted
    # order eventually and also a current and next rank attribute to help with
    # sorting 
    # suffixes = {
    #   0: {
    #       "suffix": "banana",
    #       "current_rank": None,
    #       "next_rank": None
    #   },
    #   1: {..}
    # }
    suffixes = []

    # generate all suffixes for n and set current rank for first character and
    # next rank for second character
    for i in range(n_len):
        suffixes.append((i, {}))
        suffixes[i][1]["suffix"] = n[i:]
        suffixes[i][1]["current_rank"] = ord(suffixes[i][1]["suffix"][0])
        if len(suffixes[i][1]["suffix"]) > 1:
            suffixes[i][1]["next_rank"] = ord(suffixes[i][1]["suffix"][1])
        else:
            suffixes[i][1]["next_rank"] = -1

    # sort the suffixes by the first two characters i.e. current and next rank.
    # Leverage the sorted() with custom key to sort the tuples by current/next
    # rank. Sorted returns a list of tuples.
    suffixes = sorted(suffixes, key=lambda x: (x[1]["current_rank"], x[1]["next_rank"]))

    # Now that first two characters are sorted, calculate current/next rank and
    # sort first 4, 8.. etc characters until 2*n
    k = 4
    for k in range(4, 2 * n_len, 2 * k):
        # store previous rank pair to use it to set the current rank
        prev_rank_pair = str(suffixes[0][1]["current_rank"]) + str(suffixes[0][1]["next_rank"])
        # set current rank of first suffix to 0
        suffixes[0][1]["current_rank"] = 0

        # To make the lookup easier for getting the current rank of a suffix
        # to be able to set it as the next rank, maintain a hash table with
        # suffix as the key and current rank as the value
        curr_rank_ht = {}
        curr_rank_ht[suffixes[0][1]["suffix"]] = 0

        # Loop through suffix array and set the current rank based on current
        # rank pair/previous rank pair comparison.
        for i in range(1, len(suffixes)):
            current_rank_pair = str(suffixes[i][1]["current_rank"]) + str(suffixes[i][1]["next_rank"])
            # if current and previous are same rank pairs, set current rank of
            # the current suffix to current rank of previous suffix
            if current_rank_pair == prev_rank_pair:
                suffixes[i][1]["current_rank"] = suffixes[i-1][1]["current_rank"]
            # else add 1 to the current rank of previous suffix and set it as
            # current rank of current suffix.
            else:
                suffixes[i][1]["current_rank"] = suffixes[i-1][1]["current_rank"] + 1

            # set previous rank pair to the current rank pair for the next
            # iteration check.
            prev_rank_pair = current_rank_pair

            curr_rank_ht[suffixes[i][1]["suffix"]] = suffixes[i][1]["current_rank"]

        # Loop through suffix array and set the next rank based on the current
        # rank of suffix[k/2:] and if no such suffix exists set it to -1
        for i in range(len(suffixes)):
            sub_suffix = suffixes[i][1]["suffix"][k//2:]
            if sub_suffix in curr_rank_ht:
                suffixes[i][1]["next_rank"] = curr_rank_ht[sub_suffix]
            else:
                suffixes[i][1]["next_rank"] = -1
    

        # Now that we have set both current and next rank, sort the suffix array
        # using those two values
        suffixes = sorted(suffixes, key=lambda x: (x[1]["current_rank"], x[1]["next_rank"]))

    suffix_array = []
    for i in suffixes:
        suffix_array.append(i[0])
        # print(i[1]["suffix"])

    return suffix_array

n = "banana"
suffix_array = prefix_doubling_suffix_array(n)
print(suffix_array)