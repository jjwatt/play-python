# Which are in?

# Given two arrays of strings a1 and a2 return a sorted array r in
# lexicographical order of the strings of a1 which are substrings of strings of
# a2.

# #Example 1:
# a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# returns ["arp", "live", "strong"]


# #Example 2:
# a1 = ["tarp", "mice", "bull"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# returns []
# Notes:
#     Arrays are written in "general" notation. See "Your Test Cases" for
#     examples in your language.

#     In Shell bash a1 and a2 are strings. The return is a string where words
#     are separated by commas.

#     Beware: r must be without duplicates.
#     Don't mutate the inputs.

def whicharein(a1, a2):
    return sorted(list(set(i for i in a1 for j in a2 if i in j)))
def whicharein2(a1, a2):
    # with set comp
    return sorted(list({i for i in a1 for j in a2 if i in j}))

# Delete occurrences of an element if it occurs more than n times.
# Enough is enough!

# Alice and Bob were on a holiday. Both of them took many pictures of the
# places they've been, and now they want to show Charlie their entire
# collection. However, Charlie doesn't like these sessions, since the motive
# usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells
# them that he will only sit during the session if they show the same motive at
# most N times. Luckily, Alice and Bob are able to encode the motive as a
# number. Can you help them to remove numbers such that their list contains
# each number only up to N times, without changing the order? Task

# Given a list lst and a number N, create a new list that contains each number
# of lst at most N times without reordering. For example if N = 2, and the
# input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since
# this would lead to 1 and 2 being in the result 3 times, and then take 3,
# which leads to [1,2,3,1,2,3].

# Example:
#  delete_nth ([1,1,1,1],2) # return [1,1]
#  delete_nth ([20,37,20,21],1) # return [20,37,21]


def delete_nthlc(order, max_e):
    return [o for i,o in enumerate(order)
            if order[:i].count(o) < max_e ]

def delete_nth(lst, N):
    newlst = []
    for i in lst:
        if newlst.count(i) < N:
            newlst.append(i)
    return newlst

def delete_nthr(lst, N):
    newlst = list(reversed(lst))
    def rec(l):
        if len(l) < 2:
            return l
        head = l[0]
        tail = l[1:]
        if tail.count(head) < N:
            return [head] + rec(tail)
        else:
            return rec(tail)
    return list(reversed(rec(newlst)))

# Array.diff Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b.

# array_diff([1,2],[1]) == [2]

# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(l1, l2):
    return [i for i in l1 if i not in l2]

## Maximum subarray sum

# The maximum sum subarray problem consists in finding the maximum sum of a
# contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]

# Easy case is when the list is made up of only positive numbers and the
# maximum sum is the sum of the whole array. If the list is made up of only
# negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list
# or array is also a valid sublist/subarray.

def max_sequence(arr):
    best_sum = 0
    current_sum = 0
    if not arr:
        return 0
    for i in arr:
        current_sum = max(0, current_sum + i)
        best_sum = max(best_sum, current_sum)
    return best_sum

## Take a Ten Minute Walk
# You live in the city of Cartesia where all roads are laid out in a perfect
# grid. You arrived ten minutes too early to an appointment, so you decided to
# take the opportunity to go for a short walk. The city provides its citizens
# with a Walk Generating App on their phones -- everytime you press the button
# it sends you an array of one-letter strings representing directions to walk
# (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each
# letter (direction) and you know it takes you one minute to traverse one city
# block, so create a function that will return true if the walk the app gives
# you will take you exactly ten minutes (you don't want to be early or late!)
# and will, of course, return you to your starting point. Return false
# otherwise.

#     Note: you will always receive a valid array containing a random
#     assortment of direction letters ('n', 's', 'e', or 'w' only). It will
#     never give you an empty array (that's not a walk, that's standing
#     still!).

def is_valid_walk(walk):
    '''Returns True if the walk is valid.'''
    rules = { 'n': (1,0), 's': (-1,0), 'e': (0,1), 'w': (0,-1) }
    start = (0, 0)
    loc = start
    counter = 0
    for i in walk:
        loc = (loc[0] + rules[i][0], loc[1] + rules[i][1])
        counter = counter + 1
    return counter == 10 and loc == start

def is_valid_walk_tr(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

import random
# myrandom10list = random.choices(range(1, 50), k=10)
def createlistofrandos(n, rng=None):
    if rng is None:
        rng = (1, 255)
    return random.choices(range(*rng), k=n)
