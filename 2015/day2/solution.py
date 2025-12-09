def part1(input_file: str) -> int:
    with open(input_file, "r") as file:
        lines = file.readlines()

    total = 0
    for line in lines:
        l, w, h = map(int, line.split("x"))
        area = 2*l*w + 2*w*h + 2*h*l
        extra = min(l*w, w*h, h*l)
        total += area + extra
    return total

def part2(input_file: str) -> int:
    with open(input_file, "r") as file:
        lines = file.readlines()
    total = 0
    for line in lines:
        l, w, h = map(int, line.split("x"))
        perimeter = 2*(l+w+h) - 2*max(l, w, h)
        volume = l*w*h
        total += perimeter + volume
    return total

def main():
    solution = part1("day2/input.txt")
    print(f"Part 1: {solution}")
    solution = part2("day2/input.txt")
    print(f"Part 2: {solution}")

if __name__ == "__main__":
    main()