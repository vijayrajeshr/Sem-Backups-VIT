import sys
# Use sys.stdin.readline for fast input, crucial for avoiding Time Limit Exceeded (TLE) errors.
input = sys.stdin.readline

def apply_gravity(grid):
    """
    Applies the effect of gravity to the grid. Uses list comprehension for speed.
    """
    if not grid:
        return []

    M = len(grid)    
    N = len(grid[0]) 

    # Initialize the new grid as a list of lists of characters
    new_grid = [['.' for _ in range(N)] for _ in range(M)]

    # Process column by column
    for j in range(N):
        stone_count = 0
        # 1. Count the stones in the current column (j)
        for i in range(M):
            if grid[i][j] == '*':
                stone_count += 1

        # 2. Place the stones at the bottom: 
        # Stones occupy rows from (M - stone_count) to (M - 1)
        # We can calculate the starting row for the stones:
        start_row_for_stones = M - stone_count
        
        for i in range(start_row_for_stones, M):
            new_grid[i][j] = '*'
            
    return new_grid

def rotate_right(grid):
    """
    Rotates the grid 90 degrees clockwise (right). (i, j) -> (j, M - 1 - i).
    """
    M = len(grid)
    N = len(grid[0])
    
    # New grid dimensions: N rows, M columns
    new_grid = [['.' for _ in range(M)] for _ in range(N)]

    for i in range(M):
        for j in range(N):
            if grid[i][j] == '*':
                # Calculate new position
                new_r = j
                new_c = M - 1 - i
                new_grid[new_r][new_c] = '*'

    return new_grid

def rotate_left(grid):
    """
    Rotates the grid 90 degrees counter-clockwise (left). (i, j) -> (N - 1 - j, i).
    """
    M = len(grid)
    N = len(grid[0])
    
    # New grid dimensions: N rows, M columns
    new_grid = [['.' for _ in range(M)] for _ in range(N)]

    for i in range(M):
        for j in range(N):
            if grid[i][j] == '*':
                # Calculate new position
                new_r = N - 1 - j
                new_c = i
                new_grid[new_r][new_c] = '*'

    return new_grid

def solve():
    # --- 1. Read Initial Dimensions M and N ---
    try:
        # Read and parse the first line (M N)
        dimensions = input().split()
        if not dimensions: return
            
        M = int(dimensions[0])
        N = int(dimensions[1])
    except:
        return # Handle potential errors during initial read
        
    # --- 2. Read Initial Box Configuration ---
    current_grid = []
    for _ in range(M):
        # Read lines quickly
        line = input().strip().replace(' ', '')
        # Store as list of characters for mutable state
        current_grid.append(list(line))
    
    # --- 3. Read K (number of instructions) ---
    try:
        K_line = input().strip()
        K = int(K_line) if K_line else 0
    except:
        K = 0

    # --- 4. Process K Instructions ---
    for _ in range(K):
        try:
            instruction = input().strip()
        except:
            break
            
        # The rotation step always happens first
        if instruction == 'right':
            current_grid = rotate_right(current_grid)
        elif instruction == 'left':
            current_grid = rotate_left(current_grid)
        else:
            continue

        # After rotation, the gravity step always happens next
        current_grid = apply_gravity(current_grid)

    # --- 5. Print Final Configuration ---
    # Convert the list of characters back to strings for output
    for row in current_grid:
        # Print without extra spaces
        sys.stdout.write("".join(row) + '\n')
        
if __name__ == "__main__":
    solve()
