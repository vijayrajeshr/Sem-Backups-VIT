def apply_gravity(grid):
    """
    Applies the effect of gravity to the current grid. 
    Stones ('*') fall down to the lowest possible position in each column.
    """
    if not grid:
        return []

    # Get the current dimensions of the grid
    M = len(grid)    # Number of rows
    N = len(grid[0]) # Number of columns

    new_grid = []
    # Initialize the new grid with blank spaces
    for i in range(M):
        new_grid.append(['.' for _ in range(N)])

    # Process column by column
    for j in range(N):
        stone_count = 0
        # 1. Count the stones in the current column (j)
        for i in range(M):
            if grid[i][j] == '*':
                stone_count += 1

        # 2. Place the stones at the bottom of the column in the new grid
        # Stones will start at row M - stone_count and fill up to M-1
        
        # current_row_index will track where the next stone should be placed
        # Start placing from the bottom-most row (M-1) upwards
        current_row_index = M - 1 

        # Place the stones
        for s in range(stone_count):
            new_grid[current_row_index][j] = '*'
            current_row_index -= 1 # Move one row up

        # The remaining rows above the stones are already set to '.' from initialization

    return new_grid

def rotate_right(grid):
    """
    Rotates the grid 90 degrees clockwise (right).
    An M x N grid becomes an N x M grid.
    The element at (i, j) moves to the new position (j, M - 1 - i).
    """
    M = len(grid)
    N = len(grid[0])
    
    # The new grid has N rows and M columns
    new_grid = []
    for i in range(N):
        new_grid.append(['.' for _ in range(M)])

    # Iterate through the old grid (i, j)
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '*':
                # Calculate new row (new_r) and new column (new_c)
                new_r = j
                new_c = M - 1 - i
                new_grid[new_r][new_c] = '*'

    return new_grid

def rotate_left(grid):
    """
    Rotates the grid 90 degrees counter-clockwise (left).
    An M x N grid becomes an N x M grid.
    The element at (i, j) moves to the new position (N - 1 - j, i).
    """
    M = len(grid)
    N = len(grid[0])
    
    # The new grid has N rows and M columns
    new_grid = []
    for i in range(N):
        new_grid.append(['.' for _ in range(M)])

    # Iterate through the old grid (i, j)
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '*':
                # Calculate new row (new_r) and new column (new_c)
                new_r = N - 1 - j
                new_c = i
                new_grid[new_r][new_c] = '*'

    return new_grid

def solve():
    # --- 1. Read Initial Dimensions M and N ---
    try:
        # Read the first line (M N)
        dimensions = input().split()
        if not dimensions:
            return
            
        M = int(dimensions[0])
        N = int(dimensions[1])
    except EOFError:
        return
    except Exception:
        return
        
    # --- 2. Read Initial Box Configuration ---
    current_grid = []
    for _ in range(M):
        # Read M lines of the grid. We use .replace(' ', '') to handle
        # input where characters are space-separated, but we store them 
        # contiguously as per the examples.
        line = input().strip().replace(' ', '')
        # Convert the string into a list of characters for easy modification
        current_grid.append(list(line))
    
    # --- 3. Read K (number of instructions) ---
    try:
        K = int(input().strip())
    except Exception:
        K = 0

    # --- 4. Process K Instructions ---
    for _ in range(K):
        try:
            instruction = input().strip()
        except EOFError:
            break
            
        # The rotation step always happens first
        if instruction == 'right':
            current_grid = rotate_right(current_grid)
        elif instruction == 'left':
            current_grid = rotate_left(current_grid)
        else:
            # Skip if the instruction is invalid
            continue

        # After rotation, the gravity step always happens next
        current_grid = apply_gravity(current_grid)

    # --- 5. Print Final Configuration ---
    # Convert the list of characters back to strings for output
    for row in current_grid:
        print("".join(row))

if __name__ == "__main__":
    solve()
