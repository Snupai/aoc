def part1(input_file: str) -> int:
    with open(input_file, "r") as file:
        lines = file.readlines()
    # We'll only consider the first line of input (the instructions)
    instructions = lines[0].strip()
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    for c in instructions:
        if c == ">":
            x += 1
        elif c == "<":
            x -= 1
        elif c == "^":
            y += 1
        elif c == "v":
            y -= 1
        visited.add((x, y))
    return len(visited)

def part2(input_file: str) -> int:
    with open(input_file, "r") as file:
        lines = file.readlines()
    # We'll only consider the first line of input (the instructions)
    instructions = lines[0].strip()
    
    # Both Santa and Robo-Santa start at (0, 0)
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    visited = set()
    visited.add((0, 0))  # Starting house gets 2 presents
    
    for i, c in enumerate(instructions):
        # Santa takes even-indexed instructions, Robo-Santa takes odd-indexed
        if i % 2 == 0:
            # Santa moves
            if c == ">":
                santa_x += 1
            elif c == "<":
                santa_x -= 1
            elif c == "^":
                santa_y += 1
            elif c == "v":
                santa_y -= 1
            visited.add((santa_x, santa_y))
        else:
            # Robo-Santa moves
            if c == ">":
                robo_x += 1
            elif c == "<":
                robo_x -= 1
            elif c == "^":
                robo_y += 1
            elif c == "v":
                robo_y -= 1
            visited.add((robo_x, robo_y))
    
    return len(visited)

def main():
    solution1 = part1("day3/input.txt")
    print(f"Part 1: {solution1}")
    
    solution2 = part2("day3/input.txt")
    print(f"Part 2: {solution2}")

if __name__ == "__main__":
    main()