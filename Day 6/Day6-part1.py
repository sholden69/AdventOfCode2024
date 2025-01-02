import os
import datetime


def parse_map(file_path):
    """
    Parse the input file and find the guard's starting position and facing direction.
    """
    with open(file_path, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    guard_position = None
    guard_direction = None
    
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in directions:
                guard_position = (x, y)
                guard_direction = directions[cell]
                grid[y][x] = '.'  # Replace starting symbol with empty space
                return grid, guard_position, guard_direction
    
    raise ValueError("No guard starting position found in the map.")


def turn_right(direction):
    """
    Turn the guard 90 degrees clockwise.
    """
    turns = {
        (0, -1): (1, 0),   # Up -> Right
        (1, 0): (0, 1),    # Right -> Down
        (0, 1): (-1, 0),   # Down -> Left
        (-1, 0): (0, -1)   # Left -> Up
    }
    return turns[direction]


def simulate_patrol(grid, start_pos, start_dir):
    """
    Simulate the guard's patrol path.
    """
    width, height = len(grid[0]), len(grid)
    visited = set()
    visited_states = set()  # To detect cycles
    
    x, y = start_pos
    dx, dy = start_dir
    
    # whilst the guard is still moving inside the grid
    while 0 <= x < width and 0 <= y < height:
        visited.add((x, y))  # Mark current position as visited
        
        # Detect cycle
        state = (x, y, dx, dy)
        if state in visited_states:
            print("Cycle detected, stopping simulation.")
            break
        visited_states.add(state)
        
        # Calculate next position
        next_x, next_y = x + dx, y + dy
        
        # check for obstacle and move forward if not found
        if (
            0 <= next_x < width and
            0 <= next_y < height and
            grid[next_y][next_x] != '#'
        ):
            # Move forward
            x, y = next_x, next_y
        else:
            # Turn right
            dx, dy = turn_right((dx, dy))
    
    return visited


def mark_visited_positions(grid, visited):
    """
    Mark visited positions on the grid with 'X'.
    """
    for x, y in visited:
        grid[y][x] = 'X'
    return grid


def print_grid(grid):
    """
    Print the grid nicely.
    """
    for row in grid:
        print(''.join(row))


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    file_path = os.path.join(script_dir, "input.txt")
    
    print(f"Using input file: {file_path}")
    
    # Parse the input
    grid, guard_position, guard_direction = parse_map(file_path)
    
    # Simulate the patrol
    visited_positions = simulate_patrol(grid, guard_position, guard_direction)
    
    # Mark the grid with visited positions
    grid = mark_visited_positions(grid, visited_positions)
    
    # Print the result
    print_grid(grid)
    print(f"\nNumber of visited positions: {len(visited_positions)}")


if __name__ == '__main__':
    main()
