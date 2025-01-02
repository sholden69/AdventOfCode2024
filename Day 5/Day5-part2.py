import os
from collections import defaultdict, deque

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
input_file = os.path.join(script_dir, 'input.txt')


def parse_input(file_path):
    """
    Parse the input file into rules and updates.
    """
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    rules = []
    updates = []
    reading_updates = False
    
    for line in lines:
        if '|' in line:
            x, y = line.split('|')
            rules.append((int(x), int(y)))
        else:
            updates.append([int(page) for page in line.split(',')])
    
    return rules, updates


def is_update_valid(update, rules):
    """
    Check if an update sequence adheres to the ordering rules.
    """
    update_index = {page: i for i, page in enumerate(update)}
    
    for x, y in rules:
        if x in update and y in update:
            if update_index[x] > update_index[y]:
                return False  # Rule is violated
    
    return True


def reorder_update(update, rules):
    """
    Reorder a single update based on the ordering rules.
    """
    # Create a directed graph based on the ordering rules
    graph = defaultdict(list)

    # In-degree tracks how many dependencies each page has (how many must precede it)
    in_degree = defaultdict(int)
    
     # Convert the update list to a set for quick lookups
    pages_in_update = set(update)
    
    for x, y in rules:
        # Only consider rules where both x and y are in the current update
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)   # Add a directed edge from x to y
            in_degree[y] += 1   # Increment in-degree for y (dependency added)
    
    # Topological Sort using Kahn's Algorithm - ensures the ordering represents the dependencies
    # Reference for Kahn's algorithm: https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
    # These are pages that don't depend on any other pages and can safely start the ordering.
    # use a double-ended queue (dequeue) as need to pop from the left and append at the end.
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []
    
    # The algorithm works by repeatedly finding vertices with no incoming edges, removing them from the graph, and 
    # updating the incoming edges of the remaining vertices. This process continues until all vertices have been ordered.
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Return sorted update; fall back to default sort if something went wrong
    return sorted_update if len(sorted_update) == len(update) else sorted(update)


def middle_page(update):
    """
    Return the middle page of the update.
    """
    mid_index = len(update) // 2
    return update[mid_index]


def main():
    # Parse input into rules and updates
    rules, updates = parse_input(input_file)
    
    invalid_updates = []
    for update in updates:
        if not is_update_valid(update, rules):
            reordered = reorder_update(update, rules)
            invalid_updates.append(reordered)
    
    # Calculate the sum of middle pages of reordered invalid updates
    middle_sum = sum(middle_page(update) for update in invalid_updates)
    
    print(f"Sum of middle pages of reordered invalid updates: {middle_sum}")


if __name__ == "__main__":
    main()
