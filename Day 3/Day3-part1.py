import os
import re

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
input_file = os.path.join(script_dir, 'input.txt')


def extract_and_sum_valid_mul(file_path):
    """
    Extract all valid 'mul(X,Y)' instructions from the corrupted memory,
    calculate their results, and return the total sum.
    """
    total_sum = 0
    
    # Regular expression to match valid 'mul(X,Y)' patterns
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    
    with open(file_path, 'r') as file:
        for line in file:
            # Find all valid 'mul(X,Y)' patterns in the current line
            matches = re.findall(pattern, line)
            for match in matches:
                # Extract the two numbers from each valid match
                x, y = map(int, match[4:-1].split(','))
                total_sum += x * y  # Calculate and add the product to the total sum
    
    return total_sum


# Example usage
if __name__ == "__main__":
    result = extract_and_sum_valid_mul(input_file)
    print(f"Total sum of valid mul instructions: {result}")
