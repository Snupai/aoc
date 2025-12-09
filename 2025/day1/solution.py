from helper.markdown_printer import print_markdown, print_solution

def part1(input_file):
    with open(input_file, 'r') as file:
        input = file.read()

    instructions = input.split('\n')

    position = 50
    zero_count = 0

    for instruction in instructions:
        if not instruction:
            continue

        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100

        if position == 0:
            zero_count += 1

    return zero_count

def part2(input_file):
    with open(input_file, 'r') as file:
        input = file.read()

    instructions = input.split('\n')

    position = 50
    zero_count = 0

    for instruction in instructions:
        if not instruction:
            continue

        direction = instruction[0]
        distance = int(instruction[1:])

        prev_position = position
        if direction == 'L':
            position = (position - distance) % 100
            # Check for passing through zero
            for step in range(1, distance+1):
                point = (prev_position - step) % 100
                if point == 0:
                    zero_count += 1
        else:
            position = (position + distance) % 100
            # Check for passing through zero
            for step in range(1, distance+1):
                point = (prev_position + step) % 100
                if point == 0:
                    zero_count += 1

    return zero_count

def main():
    # print out the puzzle_1.md file
    print_markdown('day1/puzzle_1.md')
    zero_count = part1('day1/input.txt')
    print_solution(zero_count)

    print("\n\n\n")

    print_markdown('day1/puzzle_2.md')
    zero_count = part2('day1/input.txt')
    print_solution(zero_count)
