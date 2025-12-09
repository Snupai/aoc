from helper.markdown_printer import print_markdown, print_solution


def part1(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().strip()
    banks = input_data.split('\n')

    def max_joltage_for_bank(bank: str) -> int:
        digits = [int(c) for c in bank]
        k = 2
        to_remove = len(digits) - k
        stack: list[int] = []

        for d in digits:
            while stack and to_remove > 0 and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)

        chosen = stack[:k]
        return chosen[0] * 10 + chosen[1]

    max_joltages = [max_joltage_for_bank(bank) for bank in banks]
    total = sum(max_joltages)
    return total


def part2(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().strip()
    banks = input_data.split('\n')

    def max_joltage_for_bank(bank: str) -> int:
        digits = [int(c) for c in bank]
        k = 12
        if len(digits) <= k:
            value = 0
            for d in digits:
                value = value * 10 + d
            return value

        to_remove = len(digits) - k
        stack: list[int] = []

        for d in digits:
            while stack and to_remove > 0 and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)

        chosen = stack[:k]
        value = 0
        for d in chosen:
            value = value * 10 + d
        return value
    max_joltages = [max_joltage_for_bank(bank) for bank in banks]
    total = sum(max_joltages)
    return total

def main():
    print_markdown('day3/puzzle_1.md')
    total_joltages = part1('day3/input.txt')
    print_solution(total_joltages)

    print("\n\n\n")

    print_markdown('day3/puzzle_2.md')
    total_joltages = part2('day3/input.txt')
    print_solution(total_joltages)
