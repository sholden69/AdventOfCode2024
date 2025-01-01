import os

def is_safe_report(report):
    """
    Check if a report is safe based on the given rules:
    1. The levels are either all increasing or all decreasing.
    2. Adjacent levels differ by at least 1 and at most 3.
    """
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are within the allowed range
    if not all(1 <= abs(diff) <= 3 for diff in diffs):
        return False
    
    # Check if all differences are increasing or decreasing
    if all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs):
        return True
    
    return False


def count_safe_reports(file_path):
    """
    Read a file with reports and count how many are safe.
    """
    safe_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                report = list(map(int, line.split()))
                if is_safe_report(report):
                    safe_count += 1
                    
    return safe_count


# Example usage
if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    input_file = os.path.join(script_dir, 'reports.txt')
    safe_reports = count_safe_reports(input_file)
    print(f"Number of safe reports: {safe_reports}")
