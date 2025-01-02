import itertools
import os 


def evaluate_expression(test_value, numbers):
    """
    Check if a test value can be achieved by inserting + or * operators between numbers,
    evaluated left-to-right.
    """
    operators = ['+', '*']
    for ops in itertools.product(operators, repeat=len(numbers) - 1):
        # Build the expression with current operator combination
        expression = str(numbers[0])
        for num, op in zip(numbers[1:], ops):
            expression += f' {op} {num}'
        
        # Evaluate the expression left-to-right
        try:
            result = evaluate_left_to_right(expression)
            if result == test_value:
                return True  # Valid expression found
        except ZeroDivisionError:
            continue  # Skip invalid expressions if any
    return False

def evaluate_left_to_right(expression):
    """
    Evaluate an arithmetic expression left-to-right, ignoring operator precedence.
    """
    tokens = expression.split()
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        operand = int(tokens[i + 1])
        if operator == '+':
            result += operand
        elif operator == '*':
            result *= operand
        i += 2
    return result

def total_calibration_result(filename):
    """
    Parse the file and calculate the total calibration result.
    """
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            test_value, numbers = line.split(':')
            test_value = int(test_value)
            numbers = list(map(int, numbers.split()))
            
            # Check if the test value can be achieved
            if evaluate_expression(test_value, numbers):
                total += test_value  # Add valid test value to the total
    return total

# Main function
if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    input_file = os.path.join(script_dir, 'input.txt')
    result = total_calibration_result(input_file)
    print(f"The total calibration result is: {result}")
