#Abu Sayiem
#I pledge that I abide by the Stevens Honor System.

def knapsack(capacity, items):
    '''proGiven a weight capacity for your knapsack and a list of items, returns the maximum value
of items you can steal without exceeding your knapsack’s limit.'''

    if capacity == 0:
        return 0
    elif items == []:
        return 0
    elif capacity < items[0][0]:
        return knapsack(capacity, items[1:])
    else:
        use = items[0][1] + knapsack(capacity - items[0][0], items[1:])
        lose = knapsack(capacity, items[1:])
        return max(use, lose)
    
