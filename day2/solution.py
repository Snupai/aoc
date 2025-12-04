from helper.markdown_printer import print_markdown, print_solution

def part1(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().strip()

    ranges = input_data.split(',')

    invalid_ids = []

    for id_range in ranges:
        if not id_range.strip():
            continue
        start_str, end_str = id_range.split('-')
        start = int(start_str)
        end = int(end_str)
        for id_number in range(start, end + 1):
            if is_invalid_id(id_number):
                invalid_ids.append(id_number)

    return sum(invalid_ids)

def is_invalid_id(id_number):
    s = str(id_number)
    length = len(s)

    if length == 0:
        return False

    if length % 2 != 0:
        return False

    half_length = length // 2
    first_half = s[:half_length]
    second_half = s[half_length:]

    if first_half == second_half:
        return True
    else:
        return False

def part2(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().strip()
    ranges = input_data.split(',')
    invalid_ids = []
    for id_range in ranges:
        if not id_range.strip():
            continue
        start_str, end_str = id_range.split('-')
        start = int(start_str)
        end = int(end_str)
        for id_number in range(start, end + 1):
            if is_invalid_id_part2(id_number):
                invalid_ids.append(id_number)
    return sum(invalid_ids)

def is_invalid_id_part2(id_number):
    s = str(id_number)
    length = len(s)
    if length == 0:
        return False

    for sub_len in range(1, length // 2 + 1):
        if length % sub_len != 0:
            continue

        repeats = length // sub_len
        substring = s[:sub_len]
        if substring * repeats == s and repeats >= 2:
            return True

    return False

def main():
    print_markdown('day2/puzzle_1.md')
    invalid_ids = part1('day2/input.txt')
    print_solution(invalid_ids)

    print("\n\n\n")
    
    print_markdown('day2/puzzle_2.md')
    invalid_ids = part2('day2/input.txt')
    print_solution(invalid_ids)
