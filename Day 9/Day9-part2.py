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


def identify_files_and_free_spaces(disk):
    """
    Identify files and free space spans in the disk.
    """
    files = []
    free_spaces = []
    
    i = 0
    while i < len(disk):
        if disk[i] == '.':
            # Start of a free space span
            start = i
            while i < len(disk) and disk[i] == '.':
                i += 1
            free_spaces.append((start, i - start))  # (start index, length)
        else:
            # Start of a file span
            start = i
            file_id = disk[i]
            while i < len(disk) and disk[i] == file_id:
                i += 1
            files.append((start, i - start, int(file_id)))  # (start index, length, file ID)
    
    return files, free_spaces


def move_files(disk, files, free_spaces):
    """
    Move files to the leftmost suitable free space span.
    Process files in decreasing order of file ID.
    """
    files.sort(key=lambda x: -x[2])  # Sort files by descending file ID
    
    for start, length, file_id in files:
        for free_start, free_length in free_spaces:
            if free_length >= length:
                # Move the file
                for i in range(length):
                    disk[free_start + i] = str(file_id)
                    disk[start + i] = '.'
                
                # Update free space span
                free_spaces.remove((free_start, free_length))
                if free_length > length:
                    free_spaces.append((free_start + length, free_length - length))
                free_spaces.sort()  # Keep spans ordered by position
                
                break  # Move to the next file
    
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
    
    # Step 2: Identify files and free spaces
    files, free_spaces = identify_files_and_free_spaces(disk)
    
    # Step 3: Move files
    disk = move_files(disk, files, free_spaces)
    
    # Step 4: Calculate the checksum
    checksum = calculate_checksum(disk)
    
    print(f"Filesystem checksum: {checksum}")


# Entry Point
if __name__ == "__main__":
    main()
