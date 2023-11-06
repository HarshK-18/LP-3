class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

class Node:
    def __init__(self, level, current_weight, current_value):
        self.level = level
        self.current_weight = current_weight
        self.current_value = current_value

def knapsack_branch_and_bound(items, capacity):
    items.sort(key=lambda item: item.ratio, reverse=True)

    def bound(node, current_weight, current_value, level):
        if current_weight >= capacity:
            return 0
        bound_value = current_value
        total_weight = current_weight
        i = level
        while i < len(items) and total_weight + items[i].weight <= capacity:
            total_weight += items[i].weight
            bound_value += items[i].value
            i += 1
        if i < len(items):
            bound_value += (capacity - total_weight) * items[i].ratio
        return bound_value

    def branch_and_bound_helper(node):
        nonlocal max_value
        level = node.level
        current_weight = node.current_weight
        current_value = node.current_value
        if current_weight > capacity:
            return
        if level == len(items):
            if current_value > max_value:
                max_value = current_value
            return
        if bound(node, current_weight, current_value, level) <= max_value:
            return

        # Exclude the item at the current level
        branch_and_bound_helper(Node(level + 1, current_weight, current_value))

        # Include the item at the current level
        current_weight += items[level].weight
        current_value += items[level].value
        branch_and_bound_helper(Node(level + 1, current_weight, current_value))

    max_value = 0
    branch_and_bound_helper(Node(level=0, current_weight=0, current_value=0))
    return max_value

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    items = []
    for i in range(n):
        weight, value = map(int, input(f"Enter weight and value for item {i + 1}: ").split())
        items.append(Item(weight, value))

    capacity = int(input("Enter the knapsack capacity: "))
    
    max_value = knapsack_branch_and_bound(items, capacity)
    print("Maximum value for the 0-1 Knapsack problem:", max_value)




#     Certainly! This Python code solves the 0-1 Knapsack problem using the Branch and Bound technique. Let's break down the code step by step:

# ### Classes:
# 1. **`Item` Class:**
#    ```python
#    class Item:
#        def __init__(self, weight, value):
#            self.weight = weight
#            self.value = value
#            self.ratio = value / weight
#    ```
#    - The `Item` class represents items with their weights (`weight`), values (`value`), and value-to-weight ratios (`ratio`).

# 2. **`Node` Class:**
#    ```python
#    class Node:
#        def __init__(self, level, current_weight, current_value):
#            self.level = level
#            self.current_weight = current_weight
#            self.current_value = current_value
#    ```
#    - The `Node` class represents nodes in the search tree. Each node contains the `level` of the item being considered, `current_weight`, and `current_value` of the items selected so far.

# ### `knapsack_branch_and_bound` Function:
# ```python
# def knapsack_branch_and_bound(items, capacity):
#     items.sort(key=lambda item: item.ratio, reverse=True)
#     ...
#     # function implementation
#     ...
#     return max_value
# ```

# 1. **Sorting Items:**
#    - The `items` list is sorted in descending order of the value-to-weight ratio (`ratio`) using the `sort` method and a lambda function. This step is crucial for the Branch and Bound technique as it helps in selecting items with higher value-to-weight ratios first.

# 2. **`bound` Function:**
#    ```python
#    def bound(node, current_weight, current_value, level):
#        ...
#        # bound calculation logic
#        ...
#        return bound_value
#    ```
#    - The `bound` function calculates the upper bound of the current node using the remaining capacity. It considers the items in descending order of their ratios and calculates the bound value based on the fractional inclusion of items.

# 3. **`branch_and_bound_helper` Function:**
#    ```python
#    def branch_and_bound_helper(node):
#        ...
#        # recursive branch and bound search
#        ...
#    ```
#    - The `branch_and_bound_helper` function performs the recursive Branch and Bound search. It explores the search tree by including or excluding items at each level, pruning branches if their bound values are lower than the current maximum value (`max_value`).

# 4. **Main Block:**
#    ```python
#    if __name__ == "__main__":
#        ...
#        # input processing
#        ...
#        max_value = knapsack_branch_and_bound(items, capacity)
#        print("Maximum value for the 0-1 Knapsack problem:", max_value)
#    ```
#    - In the main block, the code takes input for the number of items, their weights, values, and the knapsack capacity. It then calls the `knapsack_branch_and_bound` function with the provided inputs and prints the maximum value that can be obtained in the 0-1 Knapsack problem.

# The code uses the Branch and Bound technique to solve the 0-1 Knapsack problem efficiently by exploring the solution space and pruning branches that cannot lead to an optimal solution. It selects items with higher value-to-weight ratios first, making it a greedy approach within the context of the Branch and Bound algorithm.

# 0-1 Knapsack Problem:

# The 0-1 knapsack problem is a classic optimization problem. Given a set of items, each with a weight 
#  and a value, the goal is to determine the most valuable combination of items to include in a knapsack
#  with a limited weight capacity. In the 0-1 knapsack problem, each item can either be included (1) or 
#  not included (0), and you cannot take a fraction of an item. The objective is to maximize the total value 
#  of the items in the knapsack while staying within the weight capacity.

# Time and Space Complexity:

# - Time Complexity: The code uses a recursive approach to solve the problem. It explores all possible 
# combinations of items (either including or not including each item) using recursion. The time complexity
#  of this code is exponential, specifically O(2^n), where 'n' is the number of items. This is because the
#  function is called recursively for each item, and there are 2^n possible combinations to consider.

# - Space Complexity: The space complexity is determined by the depth of the call stack during the 
# recursive calls. In the worst case, the call stack can grow as deep as 'n,' resulting in a space 
# complexity of O(n).