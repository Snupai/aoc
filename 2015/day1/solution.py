def part1(input_file: str) -> int:
    with open(input_file, "r") as file:
        lines = file.readlines()
    floor = 0
    part2 = False
    for i, c in enumerate(lines[0]):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor == -1 and not part2:
            part2 = True
            print(f"Part 2: {i + 1}")
    print(f"Part 1: {floor}")


def main():
    solution = part1("day1/input.txt")
    print(solution)

if __name__ == "__main__":
    main()