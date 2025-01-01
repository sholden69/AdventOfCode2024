import os

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
            reading_updates = True
            updates.append([int(page) for page in line.split(',')])
    
    return rules, updates


def is_update_valid(update, rules):
    """
    Check if the update sequence adheres to the ordering rules.
    """
    update_index = {page: i for i, page in enumerate(update)}
    
    for x, y in rules:
        if x in update and y in update:
            if update_index[x] > update_index[y]:
                return False  # Rule is violated
    
    return True


def middle_page(update):
    """
    Return the middle page of the update.
    """
    mid_index = len(update) // 2
    return update[mid_index]


def main():
    # Parse input into rules and updates
    rules, updates = parse_input(input_file)
    
    valid_updates = []
    for update in updates:
        if is_update_valid(update, rules):
            valid_updates.append(update)
    
    # Calculate the sum of middle pages of valid updates
    middle_sum = sum(middle_page(update) for update in valid_updates)
    
    print(f"Sum of middle pages of valid updates: {middle_sum}")


if __name__ == "__main__":
    main()
