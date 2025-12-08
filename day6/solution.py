from helper.markdown_printer import print_markdown, print_solution
import re

def part1(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().strip().split('\n')
    
    # Separate number lines from operation line
    number_lines = lines[:-1]  # All lines except the last
    operation_line = lines[-1]  # Last line contains operations
    
    # Find the maximum width
    max_width = max(len(line) for line in lines)
    
    # Pad all lines to the same width
    padded_lines = [line.ljust(max_width) for line in lines]
    padded_number_lines = padded_lines[:-1]
    padded_operation_line = padded_lines[-1]
    
    # Process column by column to identify problem boundaries
    problem_regions = []
    current_region_start = None
    
    for col in range(max_width):
        # Extract characters from this column
        column_chars = []
        for line in padded_number_lines:
            column_chars.append(line[col])
        
        # Check if this column is a separator (all spaces in number lines)
        is_separator = all(c == ' ' for c in column_chars)
        
        if is_separator:
            # If we have a current region, close it
            if current_region_start is not None:
                problem_regions.append((current_region_start, col))
                current_region_start = None
        else:
            # This column is part of a problem
            if current_region_start is None:
                current_region_start = col
    
    # Don't forget the last region
    if current_region_start is not None:
        problem_regions.append((current_region_start, max_width))
    
    # Process each problem region
    total = 0
    for start_col, end_col in problem_regions:
        # Extract the region for each line
        region_lines = [line[start_col:end_col] for line in padded_number_lines]
        region_operation = padded_operation_line[start_col:end_col]
        
        # Extract numbers from each number line
        numbers = []
        for line in region_lines:
            # Find all sequences of digits
            matches = re.findall(r'\d+', line)
            for match in matches:
                numbers.append(int(match))
        
        # Extract operation (should be * or +)
        op = None
        for char in region_operation:
            if char in ['*', '+']:
                op = char
                break
        
        # Calculate result
        if op == '*':
            result = 1
            for num in numbers:
                result *= num
        elif op == '+':
            result = sum(numbers)
        else:
            result = 0
        
        total += result
    
    return total

def part2(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().strip().split('\n')
    
    # Separate number lines from operation line
    number_lines = lines[:-1]  # All lines except the last
    operation_line = lines[-1]  # Last line contains operations
    
    # Find the maximum width
    max_width = max(len(line) for line in lines)
    
    # Pad all lines to the same width
    padded_lines = [line.ljust(max_width) for line in lines]
    padded_number_lines = padded_lines[:-1]
    padded_operation_line = padded_lines[-1]
    
    # Process column by column to identify problem boundaries
    problem_regions = []
    current_region_start = None
    
    for col in range(max_width):
        # Extract characters from this column
        column_chars = []
        for line in padded_number_lines:
            column_chars.append(line[col])
        
        # Check if this column is a separator (all spaces in number lines)
        is_separator = all(c == ' ' for c in column_chars)
        
        if is_separator:
            # If we have a current region, close it
            if current_region_start is not None:
                problem_regions.append((current_region_start, col))
                current_region_start = None
        else:
            # This column is part of a problem
            if current_region_start is None:
                current_region_start = col
    
    # Don't forget the last region
    if current_region_start is not None:
        problem_regions.append((current_region_start, max_width))
    
    # Process each problem region
    total = 0
    for start_col, end_col in problem_regions:
        # Extract the region for each line
        region_lines = [line[start_col:end_col] for line in padded_number_lines]
        region_operation = padded_operation_line[start_col:end_col]
        
        # Read numbers right-to-left, column by column
        # Each column (read top-to-bottom) represents one number
        # Most significant digit is at the top, least significant at the bottom
        numbers = []
        region_width = end_col - start_col
        
        # Process columns from right to left
        for col_offset in range(region_width - 1, -1, -1):
            # Read digits from top to bottom in this column
            digits = []
            for row in range(len(region_lines)):
                if col_offset < len(region_lines[row]):
                    char = region_lines[row][col_offset]
                    if char.isdigit():
                        digits.append(char)
                    # If we hit a space after digits, we might stop (but let's collect all digits first)
            
            # If we found digits in this column, form a number
            # Most significant digit is at the top (first in digits list)
            if digits:
                num_str = ''.join(digits)
                numbers.append(int(num_str))
        
        # Extract operation (should be * or +)
        op = None
        for char in region_operation:
            if char in ['*', '+']:
                op = char
                break
        
        # Calculate result
        if op == '*':
            result = 1
            for num in numbers:
                result *= num
        elif op == '+':
            result = sum(numbers)
        else:
            result = 0
        
        total += result
    
    return total

def main():
    print_markdown('day6/puzzle_1.md')
    result = part1('day6/input.txt')
    print_solution(result)
    
    print("\n\n\n")
    
    print_markdown('day6/puzzle_2.md')
    result = part2('day6/input.txt')
    print_solution(result)
