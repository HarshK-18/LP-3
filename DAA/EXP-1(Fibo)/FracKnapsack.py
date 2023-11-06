class ItemValue:

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val / wt  # Use floating-point division for fractions

    def __lt__(self, other):
        return self.cost > other.cost  # Sort in non-increasing order

def fractionalKnapSack(wt, val, capacity):
    """Function to get the maximum value"""
    n = len(wt)
    iVal = [ItemValue(wt[i], val[i], i) for i in range(n)]

    # Sorting items by cost in non-increasing order
    iVal.sort()

    totalValue = 0
    for i in iVal:
        curWt = i.wt
        curVal = i.val
        if capacity - curWt >= 0:
            capacity -= curWt
            totalValue += curVal
        else:
            fraction = capacity / curWt
            totalValue += curVal * fraction
            break
    return totalValue

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    wt = []
    val = []

    print("Enter the weights:")
    for i in range(n):
        w = int(input())
        wt.append(w)

    print("Enter the Profits:")
    for i in range(n):
        v = int(input())
        val.append(v)

    capacity = int(input("Enter the capacity of the knapsack: "))

    maxValue = fractionalKnapSack(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)



#     Certainly! This Python code solves the fractional knapsack problem using a greedy algorithm. Let me explain the code step by step:

# 1. **`ItemValue` Class:**
#    ```python
#    class ItemValue:
#        def __init__(self, wt, val, ind):
#            self.wt = wt
#            self.val = val
#            self.ind = ind
#            self.cost = val / wt  # Use floating-point division for fractions

#        def __lt__(self, other):
#            return self.cost > other.cost  # Sort in non-increasing order
#    ```
#    - The `ItemValue` class represents items with their weights (`wt`), values (`val`), and indices (`ind`).
#    - The `cost` attribute is calculated as the value-to-weight ratio, indicating the value per unit weight of the item.
#    - The class also defines the less-than (`__lt__`) method to enable sorting items in non-increasing order of their cost (value-to-weight ratio).

# 2. **`fractionalKnapSack` Function:**
#    ```python
#    def fractionalKnapSack(wt, val, capacity):
#        n = len(wt)
#        iVal = [ItemValue(wt[i], val[i], i) for i in range(n)]

#        # Sorting items by cost in non-increasing order
#        iVal.sort()

#        totalValue = 0
#        for i in iVal:
#            curWt = i.wt
#            curVal = i.val
#            if capacity - curWt >= 0:
#                capacity -= curWt
#                totalValue += curVal
#            else:
#                fraction = capacity / curWt
#                totalValue += curVal * fraction
#                break
#        return totalValue
#    ```
#    - The `fractionalKnapSack` function takes three parameters: `wt` (list of item weights), `val` (list of item values), and `capacity` (maximum weight the knapsack can hold).
#    - It creates a list of `ItemValue` objects based on the input weights and values.
#    - The items are sorted in non-increasing order of their cost.
#    - The function then iterates through the sorted items, adding items to the knapsack until its capacity is exhausted. If an item cannot be fully added, a fraction of it is added based on the remaining capacity.
#    - The total value of the items in the knapsack is calculated and returned.

# 3. **Main Block:**
#    ```python
#    if __name__ == "__main__":
#        # Input: number of items, weights, values, and knapsack capacity
#        # ...
#        maxValue = fractionalKnapSack(wt, val, capacity)
#        print("Maximum value in Knapsack =", maxValue)
#    ```
#    - In the main block, the code takes input for the number of items, their weights, values, and the capacity of the knapsack.
#    - It then calls the `fractionalKnapSack` function with the provided inputs and prints the maximum value that can be obtained in the knapsack using fractional items.

# This code solves the fractional knapsack problem efficiently by sorting the items based on their value-to-weight ratio and adding them to the knapsack greedily until the capacity is exhausted. The greedy approach ensures that the most valuable items are selected first, maximizing the total value in the knapsack.

# # Theory:
# Fractional Knapsack Problem:

# The fractional knapsack problem is a variation of the knapsack problem. 
# In this problem, you are given a set of items, each with a weight and a 
# value. The goal is to determine the most valuable combination of items 
# to include in a knapsack with a limited weight capacity. Unlike the 0/1 
# knapsack problem, where you must either take an item in full or leave it,
# in the fractional knapsack problem, you can take a fraction of an item. 
# The objective is to maximize the total value of the items included while 
# staying within the weight capacity of the knapsack.

# Let's analyze the time and space complexity of the given fractional knapsack problem solution:

# ### Time Complexity:
# 1. **Input Processing:**
#    - Reading item weights and values: O(N), where N is the number of items.

# 2. **Creating `ItemValue` Objects:**
#    - Creating `ItemValue` objects for each item: O(N), where N is the number of items.

# 3. **Sorting the `iVal` List:**
#    - Sorting the list of `ItemValue` objects: O(N log N), where N is the number of items. The sorting step dominates the time complexity.

# 4. **Iterating Through Sorted Items:**
#    - Iterating through the sorted list once: O(N), where N is the number of items.

# Overall, the time complexity of the given code is **O(N log N)** due to the sorting step, where N is the number of items.

# ### Space Complexity:
# 1. **`ItemValue` Objects:**
#    - Storage for `ItemValue` objects: O(N), where N is the number of items. Each item has an associated `ItemValue` object.

# 2. **Input Lists:**
#    - Storage for item weights and values: O(N), where N is the number of items.

# 3. **Sorting Space:**
#    - Space used during sorting (typically in-place sorting): O(1) to O(log N), depending on the sorting algorithm used. The sorting is usually performed in-place and doesn't require additional space proportional to the input size.

# Overall, the space complexity of the given code is **O(N)**, where N is the number of items. The dominant factor contributing to space complexity is the storage of `ItemValue` objects and the input lists.