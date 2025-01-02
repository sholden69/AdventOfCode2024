import functools
import os


@functools.lru_cache(maxsize=None)
def evaluate_left_to_right(tokens):
    """
    Evaluate tokens left-to-right with +, *, and || operators.
    """
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        operand = tokens[i + 1]
        
        if operator == '+':
            result += int(operand)
        elif operator == '*':
            result *= int(operand)
        elif operator == '||':
            result = int(str(result) + str(operand))
        i += 2
    return result

def valid_concatenation(a, b):
    """ Check if concatenating two numbers is valid (e.g., no leading zeros). """
    return not (str(a).startswith('0') and len(str(a)) > 1)

@functools.lru_cache(maxsize=None)
def can_evaluate(test_value, numbers):
    """
    Recursive function to check if a test_value can be achieved
    using +, *, and || operators.
    """
    if len(numbers) == 1:
        return numbers[0] == test_value

    for i in range(1, len(numbers)):
        left, right = numbers[:i], numbers[i:]
        
        # Addition
        if can_evaluate(test_value - sum(left), right):
            return True
        
        # Multiplication
        product = 1
        for num in left:
            product *= num
        if product <= test_value and can_evaluate(test_value // product, right):
            return True
        
        # Concatenation
        concatenated = int(''.join(map(str, left)))
        if valid_concatenation(left[0], left[-1]) and can_evaluate(test_value - concatenated, right):
            return True
    
    return False

def total_calibration_result(filename):
    """
    Parse the file and calculate the total calibration result with optimized approach.
    """
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            test_value, numbers = line.split(':')
            test_value = int(test_value)
            numbers = tuple(map(int, numbers.split()))
            
            if can_evaluate(test_value, numbers):
                total += test_value
    return total

# Main function
if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    input_file = os.path.join(script_dir, 'input.txt')
    
    result = total_calibration_result(input_file)
    print(f"The optimized total calibration result is: {result}")
