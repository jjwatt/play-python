import random


myrandom10list = random.choices(range(1, 50), k=10)
def compsort(junk):
    """From taocp-vol3.1e p76.
    Algorithm C: Sorting by Counting.
    ((compare Kj with Ki) for 1 <= j <= i) for 1 < i <= N.
    where K is keys and i and j are indexes.
    COUNT[j] tells us where to move Rj
    Args:
      junk: A list of comparables.
    Returns:
      count: "count[j] tells us where to move junk[j]"
             "The invers of the permutation p(1)...p(n) is
             specified in the COUNT table.
    """
    # Set COUNT[1] through COUNT[N] to 0.
    N = len(junk) - 1
    count = [0 for i in junk]
    i = N
    while i >= 1:
        j = i - 1
        while j >= 0:
            print("i, j: ", i, j)
            if junk[i] < junk[j]:
                count[j] = count[j] + 1
            else:
                count[i] = count[i] + 1
            j = j - 1
        i = i - 1
    return count
