import os

# Construct the file path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")


def parse_map(file_path):
    """
    Parse the topographic map from the input file into a grid of integers.
    """
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file if line.strip()]


def is_within_bounds(x, y, grid):
    """
    Check if the given (x, y) coordinates are within grid bounds.
    """
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def dfs(grid, x, y, visited):
    """
    Perform a DFS to explore valid hiking trails.
    Valid trails increase by exactly 1 at each step.
    """
    stack = [(x, y)]
    reachable_nines = set()
    
    while stack:
        cx, cy = stack.pop()
        current_height = grid[cx][cy]
        
        if current_height == 9:
            reachable_nines.add((cx, cy))
            continue
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
            nx, ny = cx + dx, cy + dy
            if is_within_bounds(nx, ny, grid) and (nx, ny) not in visited:
                if grid[nx][ny] == current_height + 1:
                    visited.add((nx, ny))
                    stack.append((nx, ny))
    
    return len(reachable_nines)


def calculate_trailhead_scores(grid):
    """
    Calculate the sum of scores for all trailheads on the map.
    """
    visited = set()
    total_score = 0
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0 and (x, y) not in visited:
                visited.add((x, y))
                score = dfs(grid, x, y, visited)
                total_score += score
    
    return total_score


def main():
    # Parse the map from the input file
    grid = parse_map(file_path)
    
    # Calculate the sum of trailhead scores
    total_score = calculate_trailhead_scores(grid)
    
    print(f"Total trailhead score: {total_score}")


# Entry Point
if __name__ == "__main__":
    main()
