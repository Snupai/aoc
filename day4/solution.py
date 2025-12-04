from helper.markdown_printer import print_markdown, print_solution


def part1(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().rstrip("\n")

    grid = input_data.split("\n")
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def neighbors(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

    accessible_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            adjacent_rolls = sum(
                1 for nr, nc in neighbors(r, c) if grid[nr][nc] == "@"
            )

            if adjacent_rolls < 4:
                accessible_count += 1

    return accessible_count

def part2(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().rstrip("\n")

    grid = [list(row) for row in input_data.split("\n")]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def neighbors(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

    removed_total = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "@":
                    continue

                adjacent_rolls = sum(
                    1 for nr, nc in neighbors(r, c) if grid[nr][nc] == "@"
                )

                if adjacent_rolls < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = "."

        removed_total += len(to_remove)

    return removed_total

def main():
    print_markdown('day4/puzzle_1.md')
    accessible_count = part1('day4/input.txt')
    print_solution(accessible_count)

    print("\n\n\n")

    print_markdown('day4/puzzle_2.md')
    removed_total = part2('day4/input.txt')
    print_solution(removed_total)