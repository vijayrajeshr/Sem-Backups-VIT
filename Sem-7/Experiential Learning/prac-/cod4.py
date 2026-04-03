def apply_gravity(grid):
    """Applies gravity to the current grid (O(M*N))."""
    if not grid: return []

    M, N = len(grid), len(grid[0])
    new_grid = [['.' for _ in range(N)] for _ in range(M)]

    for j in range(N):
        stone_count = sum(1 for i in range(M) if grid[i][j] == '*')
        start_row = M - stone_count
        
        for i in range(start_row, M):
            new_grid[i][j] = '*'
            
    return new_grid

def rotate_right(grid):
    """Rotates the grid 90 degrees clockwise (O(M*N)). (i, j) -> (j, M - 1 - i)"""
    M, N = len(grid), len(grid[0])
    new_grid = [['.' for _ in range(M)] for _ in range(N)]

    for i in range(M):
        for j in range(N):
            if grid[i][j] == '*':
                new_grid[j][M - 1 - i] = '*'
    return new_grid

def rotate_left(grid):
    """Rotates the grid 90 degrees counter-clockwise (O(M*N)). (i, j) -> (N - 1 - j, i)"""
    M, N = len(grid), len(grid[0])
    new_grid = [['.' for _ in range(M)] for _ in range(N)]

    for i in range(M):
        for j in range(N):
            if grid[i][j] == '*':
                new_grid[N - 1 - j][i] = '*'
    return new_grid

# Helper to convert a mutable list of lists to an immutable tuple of tuples for hashing
def grid_to_hashable(grid):
    return tuple(tuple(row) for row in grid)

# Helper to convert back from hashable state to mutable grid
def hashable_to_grid(h_grid):
    return [list(row) for row in h_grid]

def solve():
    # Helper to get input line
    def get_input():
        try:
            return input().strip()
        except:
            return ""

    # --- 1. Read Initial Dimensions M and N ---
    dimensions = get_input().split()
    if not dimensions: return
    try:
        M, N = int(dimensions[0]), int(dimensions[1])
    except:
        return
        
    # --- 2. Read Initial Box Configuration ---
    current_grid = []
    for _ in range(M):
        # Robustly parse the input line, splitting by space and then flattening
        line_parts = get_input().split()
        row = [char for part in line_parts for char in part if char in ('*', '.')]
        # Fallback for non-space-separated input
        if not row and line_parts: 
             row = list("".join(line_parts))

        if row: # Only append if we successfully parsed a row
            current_grid.append(row)
        
    # --- 3. Read K and all Instructions ---
    instructions = []
    K_line = get_input()
    K = 0
    if K_line:
        try:
            K = int(K_line)
        except:
            pass
        
    for _ in range(K):
        instructions.append(get_input())
        
    # --- 4. Cycle Detection and Simulation ---
    
    # Store the state (tuple of tuples) mapped to the step index (0-based)
    # The key is the grid configuration, the value is the step index (i)
    seen_states = {grid_to_hashable(current_grid): 0}
    
    # Store the grid at each step, indexed by step number (0-based)
    state_history = [current_grid]
    
    cycle_found = False
    cycle_start_index = -1
    cycle_length = -1
    
    # Simulate step-by-step
    for i in range(1, K + 1):
        instruction_index = i - 1
        
        # --- Apply the transformation (Rotation + Gravity) ---
        instruction = instructions[instruction_index]
        
        # 4a. ROTATION
        if instruction == 'right':
            next_grid = rotate_right(current_grid)
        elif instruction == 'left':
            next_grid = rotate_left(current_grid)
        else:
            # Handle empty or invalid instruction line (should not happen in valid test case)
            current_grid = current_grid 
            continue 

        # 4b. GRAVITY
        current_grid = apply_gravity(next_grid)

        # --- Check for Cycle ---
        hashable_state = grid_to_hashable(current_grid)
        
        if hashable_state in seen_states:
            # Cycle found!
            cycle_start_index = seen_states[hashable_state]
            cycle_length = i - cycle_start_index
            cycle_found = True
            break # Exit the loop, we don't need to simulate any more
        
        # Store new state
        seen_states[hashable_state] = i
        state_history.append(current_grid)
        
    # --- 5. Determine Final State ---
    
    final_grid = current_grid # Default if K is small or no cycle found
    
    if cycle_found:
        # The number of steps remaining after the cycle starts
        remaining_steps = K - cycle_start_index
        # The position within the cycle (0-based index from cycle start)
        position_in_cycle = remaining_steps % cycle_length
        
        # The final state index in the history list
        final_history_index = cycle_start_index + position_in_cycle
        
        # Retrieve the final grid state from the history
        final_grid = state_history[final_history_index]
        
    # --- 6. Print Final Configuration ---
    output = []
    for row in final_grid:
        output.append("".join(row))
        
    print('\n'.join(output))

if __name__ == "__main__":
    solve()
