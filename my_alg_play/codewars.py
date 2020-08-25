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

import random
# myrandom10list = random.choices(range(1, 50), k=10)
def createlistofrandos(n, rng=None):
    if rng is None:
        rng = (1, 255)
    return random.choices(range(*rng), k=n)
