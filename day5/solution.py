from helper.markdown_printer import print_markdown, print_solution

def part1(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().strip()
    fresh_ranges = input_data.split('\n\n')[0].split('\n')
    available_ids = input_data.split('\n\n')[1].split('\n')
    
    ranges = []
    for id_range in fresh_ranges:
        if id_range:
            start, end = id_range.split('-')
            ranges.append((int(start), int(end)))
    
    fresh_count = 0
    for available_id_str in available_ids:
        if not available_id_str:
            continue
        available_id = int(available_id_str)
        for start, end in ranges:
            if start <= available_id <= end:
                fresh_count += 1
                break
    
    return fresh_count

def part2(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().strip()
    fresh_ranges = input_data.split('\n\n')[0].split('\n')
    
    ranges = []
    for id_range in fresh_ranges:
        if id_range:
            start, end = id_range.split('-')
            ranges.append((int(start), int(end)))
    
    ranges.sort()
    
    merged = []
    for start, end in ranges:
        if not merged:
            merged.append((start, end))
        else:
            last_start, last_end = merged[-1]
            if start <= last_end + 1:
                merged[-1] = (last_start, max(last_end, end))
            else:
                merged.append((start, end))
    
    count_fresh_ids = 0
    for start, end in merged:
        count_fresh_ids += (end - start + 1)
    
    return count_fresh_ids

def main():
    print_markdown('day5/puzzle_1.md')
    result = part1('day5/input.txt')
    print_solution(result)
    print("\n\n\n")
    print_markdown('day5/puzzle_2.md')
    result = part2('day5/input.txt')
    print_solution(result)
