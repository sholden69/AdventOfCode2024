import itertools
import os 

def evaluate_expression(test_value, numbers):
    """
    Check if a test value can be achieved by inserting operators between the numbers.
    """
    # Define the operators available
    operators = ['+', '*']
    
    # Generate all possible combinations of operators
    for ops in itertools.product(operators, repeat=len(numbers) - 1):
        # Construct the expression as a string
        expression = str(numbers[0])
        for num, op in zip(numbers[1:], ops):
            expression += f' {op} {num}'
        # Evaluate the expression left-to-right
        result = eval(expression)
        if result == test_value:
            return True  # Found a valid combination
    return False

def total_calibration_result(filename):
    """
    Parse the file and calculate the total calibration result.
    """
    total = 0
    
    with open(filename, 'r') as file:
        for line in file:
            # Parse the input line
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            test_value, numbers = line.split(':')
            test_value = int(test_value)
            numbers = list(map(int, numbers.split()))
            
            # Check if the test value can be achieved
            if evaluate_expression(test_value, numbers):
                total += test_value
    
    return total

# Main function
if __name__ == "__main__":
    # Input file containing the puzzle input
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    input_file = os.path.join(script_dir, 'input.txt')

    result = total_calibration_result(input_file)
    print(f"The total calibration result is: {result}")
