import os

# Construct the file path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")


def parse_disk_map(disk_map):
    """
    Parse the disk map into a list of file and free space blocks.
    """
    disk = []
    file_id = 0
    
    i = 0
    while i < len(disk_map):
        # File blocks
        file_length = int(disk_map[i])
        disk.extend([str(file_id)] * file_length)
        file_id += 1
        i += 1
        
        if i < len(disk_map):
            # Free space blocks
            free_length = int(disk_map[i])
            disk.extend(['.'] * free_length)
            i += 1
    
    return disk


def compact_disk(disk):
    """
    Compact the disk by moving file blocks one at a time from right to left.
    """
    while True:
        # Find the rightmost file block
        rightmost_file = next((i for i in reversed(range(len(disk))) if disk[i] != '.'), None)
        if rightmost_file is None:
            break  # No more file blocks
        
        # Find the leftmost free space
        leftmost_free = next((i for i in range(len(disk)) if disk[i] == '.'), None)
        if leftmost_free is None or leftmost_free > rightmost_file:
            break  # No more valid moves
        
        # Move the file block
        disk[leftmost_free], disk[rightmost_file] = disk[rightmost_file], '.'
    
    return disk


def calculate_checksum(disk):
    """
    Calculate the checksum by summing position * file ID for each file block.
    """
    return sum(i * int(block) for i, block in enumerate(disk) if block != '.')


def main():
    # Read the input
    with open(file_path, 'r') as file:
        disk_map = file.readline().strip()
    
    # Step 1: Parse the disk map
    disk = parse_disk_map(disk_map)
    
    # Step 2: Compact the disk
    compacted_disk = compact_disk(disk)
    
    # Step 3: Calculate the checksum
    checksum = calculate_checksum(compacted_disk)
    
    print(f"Filesystem checksum: {checksum}")


# Entry Point
if __name__ == "__main__":
    main()
