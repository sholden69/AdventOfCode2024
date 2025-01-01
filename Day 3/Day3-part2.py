import os
import re

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
input_file = os.path.join(script_dir, 'input.txt')


def extract_and_sum_valid_mul_with_conditions(file_path):
    """
    Extract valid 'mul(X,Y)' instructions and handle 'do()' and 'don't()' conditions.
    Calculate the total sum of enabled 'mul' results.
    """
    total_sum = 0
    mul_enabled = True  # Multiplications are enabled by default
    
    # Regular expressions for mul, do, and don't instructions
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    with open(file_path, 'r') as file:
        for line in file:
            # Tokenize the line into matches for mul, do, and don't
            tokens = re.findall(f"{mul_pattern}|{do_pattern}|{dont_pattern}", line)
            
            for token in tokens:
                if token == "do()":
                    mul_enabled = True  # Enable future mul instructions
                elif token == "don't()":
                    mul_enabled = False  # Disable future mul instructions
                elif token.startswith("mul(") and mul_enabled:
                    # Extract numbers and calculate the product
                    x, y = map(int, token[4:-1].split(','))
                    total_sum += x * y
    
    return total_sum


# Example usage
if __name__ == "__main__":
    result = extract_and_sum_valid_mul_with_conditions(input_file)
    print(f"Total sum of valid enabled mul instructions: {result}")
