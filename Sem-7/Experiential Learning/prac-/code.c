#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 200
#define MAX_GRID_LEN (MAX_SIZE * MAX_SIZE + 1)
#define MAX_HISTORY 500

// Fixed-size global arrays for state management (easier for compiler)
char history_strings[MAX_HISTORY][MAX_GRID_LEN];
char history_grids[MAX_HISTORY][MAX_SIZE][MAX_SIZE];
int history_dims[MAX_HISTORY][2]; // [M, N] dimensions at this step

// --- Core Logic Functions ---

// Applies gravity in place
void apply_gravity(char grid[MAX_SIZE][MAX_SIZE], int M, int N) {
    for (int j = 0; j < N; j++) {
        int stone_count = 0;
        for (int i = 0; i < M; i++) {
            if (grid[i][j] == '*') {
                stone_count++;
            }
        }
        int start_row = M - stone_count;
        for (int i = 0; i < M; i++) {
            grid[i][j] = (i >= start_row) ? '*' : '.';
        }
    }
}

// Rotates Right: M x N -> N x M. (i, j) -> (j, M - 1 - i)
void rotate_right(const char current_grid[MAX_SIZE][MAX_SIZE], char next_grid[MAX_SIZE][MAX_SIZE], int M, int N) {
    // New dimensions are N rows and M columns
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            next_grid[i][j] = current_grid[M - 1 - j][i]; // Transpose of left rotation.
        }
    }
}

// Rotates Left: M x N -> N x M. (i, j) -> (N - 1 - j, i)
void rotate_left(const char current_grid[MAX_SIZE][MAX_SIZE], char next_grid[MAX_SIZE][MAX_SIZE], int M, int N) {
    // New dimensions are N rows and M columns
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            next_grid[i][j] = current_grid[j][N - 1 - i]; // Transpose of right rotation.
        }
    }
}

// Converts grid to string for comparison
void grid_to_string(const char grid[MAX_SIZE][MAX_SIZE], int M, int N, char *buffer) {
    int k = 0;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            buffer[k++] = grid[i][j];
        }
    }
    buffer[k] = '\0';
}

// --- Main Solver ---

int main() {
    // Use fast I/O
    if (setvbuf(stdout, NULL, _IONBF, 0) != 0) return 1;

    int M, N;
    long long K;
    
    // Read M, N
    if (scanf("%d %d", &M, &N) != 2) return 0;

    // Read initial grid
    char current_grid[MAX_SIZE][MAX_SIZE];
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            int c;
            // Read character by character, skipping whitespace (robust I/O)
            while ((c = getchar()) != EOF && (c == ' ' || c == '\n' || c == '\r'));
            if (c == EOF) return 0;
            current_grid[i][j] = (char)c;
        }
    }
    
    // Read K
    if (scanf("%lld", &K) != 1) return 0;

    // Read all instructions (only reading K or MAX_HISTORY instructions, whichever is smaller)
    char instruction_buffer[7];
    char **instructions = (char**)malloc(sizeof(char*) * (K > MAX_HISTORY ? MAX_HISTORY : K));
    long long instructions_read = 0;

    for (long long i = 0; i < (K > MAX_HISTORY ? MAX_HISTORY : K); i++) {
        instructions[i] = (char*)malloc(7 * sizeof(char));
        if (scanf("%6s", instructions[i]) != 1) {
            break;
        }
        instructions_read++;
    }
    
    // --- Cycle Detection and Simulation ---
    int current_M = M;
    int current_N = N;
    int history_count = 0;
    long long cycle_start_index = -1;
    long long cycle_length = -1;
    
    char next_grid[MAX_SIZE][MAX_SIZE];
    
    // Store initial state (step 0)
    grid_to_string(current_grid, current_M, current_N, history_strings[history_count]);
    memcpy(history_grids[history_count], current_grid, current_M * current_N * sizeof(char));
    history_dims[history_count][0] = current_M;
    history_dims[history_count][1] = current_N;
    history_count++;

    for (long long i = 1; i <= K; i++) {
        // If we found a cycle, or if we ran out of pre-read instructions, stop.
        if (cycle_start_index != -1 || (i - 1 >= instructions_read)) {
             break;
        }

        char *instruction = instructions[i - 1];

        // --- 1. ROTATION ---
        int next_M = current_N;
        int next_N = current_M;
        
        if (strcmp(instruction, "right") == 0) {
            rotate_right(current_grid, next_grid, current_M, current_N);
        } else if (strcmp(instruction, "left") == 0) {
            rotate_left(current_grid, next_grid, current_M, current_N);
        } else {
            // Should not happen, but prevents crash
            continue; 
        }

        // --- 2. GRAVITY ---
        apply_gravity(next_grid, next_M, next_N);
        
        // Update current state for next loop
        memcpy(current_grid, next_grid, next_M * next_N * sizeof(char));
        current_M = next_M;
        current_N = next_N;

        // --- Check for Cycle ---
        char current_grid_str[MAX_GRID_LEN];
        grid_to_string(current_grid, current_M, current_N, current_grid_str);
        
        for (int j = 0; j < history_count; j++) {
            if (history_dims[j][0] == current_M && history_dims[j][1] == current_N) {
                if (strcmp(history_strings[j], current_grid_str) == 0) {
                    cycle_start_index = j;
                    cycle_length = i - j;
                    break;
                }
            }
        }
        
        // Store new state if cycle not found and history slot available
        if (cycle_start_index == -1 && history_count < MAX_HISTORY) {
            strcpy(history_strings[history_count], current_grid_str);
            memcpy(history_grids[history_count], current_grid, current_M * current_N * sizeof(char));
            history_dims[history_count][0] = current_M;
            history_dims[history_count][1] = current_N;
            history_count++;
        }
    }

    // --- 5. Determine Final State ---
    
    if (cycle_start_index != -1) {
        long long remaining_steps = K - cycle_start_index;
        long long position_in_cycle = remaining_steps % cycle_length;
        long long final_history_index = cycle_start_index + position_in_cycle;
        
        current_M = history_dims[final_history_index][0];
        current_N = history_dims[final_history_index][1];
        memcpy(current_grid, history_grids[final_history_index], current_M * current_N * sizeof(char));
    }
    
    // --- 6. Print Final Configuration ---
    for (int i = 0; i < current_M; i++) {
        for (int j = 0; j < current_N; j++) {
            putchar(current_grid[i][j]);
        }
        putchar('\n');
    }

    // Cleanup allocated memory
    for (long long i = 0; i < instructions_read; i++) {
        free(instructions[i]);
    }
    free(instructions);

    return 0;
}
