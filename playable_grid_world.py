import random

GRID_SIZE = 10
NUM_TREASURES = 5

EMPTY = "."
AGENT = "A"
TREASURE = "T"


def create_grid(size):
    return [[EMPTY for _ in range(size)] for _ in range(size)]


def generate_positions(size, num_treasures):
    positions = set()

    while len(positions) < num_treasures + 1:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        positions.add((row, col))

    positions = list(positions)
    agent_start = positions[0]
    treasures = set(positions[1:])

    return agent_start, treasures


def build_display_grid(size, agent, treasures):
    grid = create_grid(size)

    for row, col in treasures:
        grid[row][col] = TREASURE

    row, col = agent
    grid[row][col] = AGENT

    return grid


def print_grid(grid):
    print("\n10 x 10 GRID WORLD\n")
    print("   " + " ".join(f"{i:2}" for i in range(len(grid))))

    for i, row in enumerate(grid):
        print(f"{i:2} " + " ".join(f"{cell:2}" for cell in row))


def move_agent(agent, direction):
    row, col = agent

    if direction == "w":
        row -= 1
    elif direction == "s":
        row += 1
    elif direction == "a":
        col -= 1
    elif direction == "d":
        col += 1

    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        return row, col

    return agent


def main():
    random.seed()

    agent, treasures = generate_positions(GRID_SIZE, NUM_TREASURES)
    path_cost = 0

    print("\nCollect all 5 treasure chests to win.")
    print("Controls: W = up, S = down, A = left, D = right, Q = quit")

    while treasures:
        grid = build_display_grid(GRID_SIZE, agent, treasures)
        print_grid(grid)

        print(f"\nTreasures remaining: {len(treasures)}")
        print(f"Path cost (moves): {path_cost}")

        command = input("\nMove (W/A/S/D): ").strip().lower()

        if command == "q":
            print("\nGame ended.")
            return

        if command not in {"w", "a", "s", "d"}:
            print("\nInvalid command. Use W, A, S, D, or Q.")
            continue

        old_agent = agent
        agent = move_agent(agent, command)

        if agent == old_agent:
            print("\nYou cannot move outside the grid.")
            continue

        path_cost += 1

        if agent in treasures:
            treasures.remove(agent)
            print("\nTreasure collected!")

    grid = build_display_grid(GRID_SIZE, agent, treasures)
    print_grid(grid)

    print("\nYou collected every treasure!")
    print(f"Final path cost: {path_cost} moves")


if __name__ == "__main__":
    main()
