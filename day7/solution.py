from helper.markdown_printer import print_markdown, print_solution
TEST_DATA = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""


def part1(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read()
    # Convert each line to a list for mutable assignment
    lines = [list(line) for line in input_data.strip('\n').split('\n')]
    line_length = len(lines[0])
    line_count = len(lines)

    splitter_count = 0
    
    # Find starting position
    start_x = None
    start_y = None
    for y in range(line_count):
        for x in range(line_length):
            if lines[y][x] == 'S':
                start_x = x
                start_y = y
                break
        if start_x is not None:
            break
    
    # Track active beam positions (set of x coordinates)
    active_beams = {start_x}
    
    # Process each line from top to bottom
    for y in range(line_count):
        next_beams = set()
        
        # Process each active beam
        for x in active_beams:
            # Check what's at the current position
            current_char = lines[y][x]
            
            if current_char == '^':
                splitter_count += 1
                # Splitter: beam stops here, mark adjacent positions and create new beams
                if x - 1 >= 0 and lines[y][x - 1] == '.':
                    lines[y][x - 1] = '|'
                    next_beams.add(x - 1)
                if x + 1 < line_length and lines[y][x + 1] == '.':
                    lines[y][x + 1] = '|'
                    next_beams.add(x + 1)
            else:
                # Beam continues: mark current position if empty, then continue downward
                if current_char == '.':
                    lines[y][x] = '|'
                if y + 1 < line_count:
                    next_beams.add(x)
        
        active_beams = next_beams
    
    print_lines(lines)
    return splitter_count

def part2(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read()
    lines = [list(line) for line in input_data.strip('\n').split('\n')]
    line_length = len(lines[0])
    line_count = len(lines)

    start_x, start_y = None, None
    for y in range(line_count):
        for x in range(line_length):
            if lines[y][x] == 'S':
                start_x, start_y = x, y
                break
        if start_x is not None:
            break

    timelines_by_row = {start_y: {start_x: 1}}
    
    for y in range(start_y, line_count - 1):
        next_timelines = {}
        
        for x, count in timelines_by_row.get(y, {}).items():
            char_below = lines[y + 1][x]
            
            if char_below == '^':
                if x - 1 >= 0:
                    next_timelines[x - 1] = next_timelines.get(x - 1, 0) + count
                if x + 1 < line_length:
                    next_timelines[x + 1] = next_timelines.get(x + 1, 0) + count
            else:
                next_timelines[x] = next_timelines.get(x, 0) + count
        
        timelines_by_row[y + 1] = next_timelines
    
    final_row = line_count - 1
    total_timelines = sum(timelines_by_row[final_row].values())
    
    return total_timelines

def print_lines(lines):
    for row in lines:
        print(''.join(row))
    print()

def main():
    print_markdown('day7/puzzle_1.md')
    result = part1('day7/input.txt')
    print_solution(result)
    
    print("\n\n\n")
    
    print_markdown('day7/puzzle_2.md')
    result = part2('day7/input.txt')
    print_solution(result)
