import itertools
import functools
import os 


@functools.lru_cache(maxsize=None)
def evaluate_left_to_right(tokens):
    """
    Evaluate a sequence of numbers and operators explicitly left-to-right.
    Supports +, *, and concatenation (||).
    """
    result = int(tokens[0])  # Start with the first number
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
    """Ensure concatenation doesn't result in invalid numbers."""
    return not (str(a).startswith('0') and len(str(a)) > 1)

def can_evaluate(test_value, numbers):
    """
    Determine if a test value can be achieved using +, *, and ||.
    """
    operators = ['+', '*', '||']
    for ops in itertools.product(operators, repeat=len(numbers) - 1):
        expression = []
        for i, op in enumerate(ops):
            expression.append(str(numbers[i]))
            expression.append(op)
        expression.append(str(numbers[-1]))
        
        try:
            result = evaluate_left_to_right(expression)
            if result == test_value:
                return True
        except (ValueError, ZeroDivisionError):
            continue  # Skip invalid states
    return False

def total_calibration_result(filename):
    """
    Parse the file and calculate the total calibration result with optimized handling.
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
                total += test_value  # Add valid test value to the total
    return total

# Main function
if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    input_file = os.path.join(script_dir, 'input.txt')
    
    result = total_calibration_result(input_file)
    print(f"The final optimized total calibration result is: {result}")
