import numpy as np

# =====================================
# CONFIGURATION
# =====================================

ROWS = 20
COLS = 10

EMPTY = 0
PERSON = 1
BLOCK = -1

NUM_BLOCKS = 15
NUM_PEOPLE = 45
STEPS = 10

CONGESTION_LIMIT = 12

# =====================================
# CREATE CORRIDOR
# =====================================

corridor = np.zeros((ROWS, COLS), dtype=int)

# =====================================
# DISPLAY FUNCTION
# =====================================

def display(grid):
    symbols = {
        EMPTY: ".",
        PERSON: "P",
        BLOCK: "X"
    }

    for row in grid:
        print(" ".join(symbols[cell] for cell in row))
    print()

# =====================================
# PLACE OBSTACLES
# =====================================

def place_blocks(grid, count):
    placed = 0

    while placed < count:

        row = np.random.randint(ROWS)
        col = np.random.randint(COLS)

        if grid[row, col] == EMPTY:
            grid[row, col] = BLOCK
            placed += 1

# =====================================
# PLACE PEOPLE
# =====================================

def place_people(grid, count):
    placed = 0

    while placed < count:

        row = np.random.randint(ROWS)
        col = np.random.randint(COLS)

        if grid[row, col] == EMPTY:
            grid[row, col] = PERSON
            placed += 1

# =====================================
# MOVE PEOPLE
# =====================================

def move_people(grid):

    new_grid = grid.copy()

    people_positions = np.argwhere(grid == PERSON)

    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

    for row,col in people_positions:

        dr,dc = directions[np.random.randint(4)]

        nr = row + dr
        nc = col + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS:

            if new_grid[nr,nc] == EMPTY:

                new_grid[nr,nc] = PERSON
                new_grid[row,col] = EMPTY

    return new_grid

# =====================================
# DENSITY REPORT
# =====================================

def density_report(grid):

    mid_row = ROWS // 2
    mid_col = COLS // 2

    zones = {
        "Top Left": np.count_nonzero(grid[:mid_row,:mid_col] == PERSON),
        "Top Right": np.count_nonzero(grid[:mid_row,mid_col:] == PERSON),
        "Bottom Left": np.count_nonzero(grid[mid_row:,:mid_col] == PERSON),
        "Bottom Right": np.count_nonzero(grid[mid_row:,mid_col:] == PERSON)
    }

    print("="*50)
    print("ZONE DENSITY")
    print("="*50)

    for zone,count in zones.items():

        status = "Normal"

        if count >= CONGESTION_LIMIT:
            status = "Congested"

        print(f"{zone:<15}: {count:2}   {status}")

    print()

    print("Highest Density :", max(zones,key=zones.get))
    print("Lowest Density  :", min(zones,key=zones.get))

# =====================================
# LOCAL DENSITY HEAT MAP
# =====================================

def risk_map(grid):

    print("\n")
    print("=" * 50)
    print("LOCAL DENSITY HEAT MAP")
    print("=" * 50)

    people = (grid == PERSON).astype(int)

    heat = np.zeros_like(people)

    # Count people in every 3x3 neighbourhood
    for i in range(ROWS):
        for j in range(COLS):

            r1 = max(0, i - 1)
            r2 = min(ROWS, i + 2)

            c1 = max(0, j - 1)
            c2 = min(COLS, j + 2)

            heat[i, j] = np.sum(people[r1:r2, c1:c2])

    print(heat)

    print("\nAverage Density :", np.mean(heat))
    print("Maximum Density :", np.max(heat))
    print("Minimum Density :", np.min(heat))

    print("\nCongestion Map")

    congestion = np.full((ROWS, COLS), ".", dtype="<U1")

    congestion[heat >= 6] = "R"      # Red
    congestion[(heat >= 3) & (heat < 6)] = "Y"   # Yellow
    congestion[heat < 3] = "G"       # Green

    for row in congestion:
        print(" ".join(row))

# =====================================
# MAIN
# =====================================

print("="*50)
print("INITIAL CORRIDOR")
print("="*50)

place_blocks(corridor,NUM_BLOCKS)
place_people(corridor,NUM_PEOPLE)

display(corridor)

for _ in range(STEPS):

    corridor = move_people(corridor)

print("="*50)
print("FINAL CORRIDOR")
print("="*50)

display(corridor)

people = np.count_nonzero(corridor == PERSON)
blocked = np.count_nonzero(corridor == BLOCK)
empty = np.count_nonzero(corridor == EMPTY)

occupancy = ((people + blocked)/corridor.size)*100

print("="*50)
print("FINAL REPORT")
print("="*50)

print("People        :",people)
print("Blocked       :",blocked)
print("Empty         :",empty)
print(f"Occupancy     : {occupancy:.2f}%")

density_report(corridor)

risk_map(corridor)