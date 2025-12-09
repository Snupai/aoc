from helper.markdown_printer import print_markdown, print_solution

INPUT_DATA = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()

def part1(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().strip()

    grid = input_data.split('\n')
    rows = len(grid)
    biggest_possible = 0
    
    for r in range(rows):
        current_row = grid[r]
        first, second = current_row.split(',')
        for c in range(r+1, rows):
            current_row = grid[c]
            third, fourth = current_row.split(',')
            erg1 = int(first) - int(third)
            erg2 = int(second) - int(fourth)
            if erg1 < 0:
                erg1 = -erg1
            if erg2 < 0:
                erg2 = -erg2
            biggest_possible = max(biggest_possible, (erg1+1) * (erg2+1))
    return biggest_possible

def part2(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().strip()
        
    grid = [tuple(map(int, point.split(','))) for point in input_data.split('\n')]
    rows = len(grid)

    # Build polygon edges (axis-aligned, closed)
    edges = []
    for r in range(rows):
        p1 = grid[r]
        p2 = grid[(r + 1) % rows]
        edges.append((p1, p2))

    def point_on_edge(pt, e):
        (x, y), (x2, y2) = e
        if x == x2:  # vertical
            return x == pt[0] and min(y, y2) <= pt[1] <= max(y, y2)
        else:  # horizontal
            return y == pt[1] and min(x, x2) <= pt[0] <= max(x, x2)

    def point_inside(pt):
        # even-odd rule; treat on-edge as inside
        for e in edges:
            if point_on_edge(pt, e):
                return True
        x, y = pt
        crossings = 0
        for (x1, y1), (x2, y2) in edges:
            if y1 == y2:  # horizontal
                continue
            if y < min(y1, y2) or y >= max(y1, y2):
                continue
            # compute x intersection of vertical ray
            xinters = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xinters > x:
                crossings += 1
        return crossings % 2 == 1

    def segments_intersect(a1, a2, b1, b2):
        # axis-aligned segments only
        ax1, ay1 = a1
        ax2, ay2 = a2
        bx1, by1 = b1
        bx2, by2 = b2

        # Normalize
        if ax1 == ax2:
            avx = ax1
            ay_low, ay_high = sorted((ay1, ay2))
        else:
            avy = ay1
            ax_low, ax_high = sorted((ax1, ax2))

        if bx1 == bx2:
            bvx = bx1
            by_low, by_high = sorted((by1, by2))
        else:
            bvy = by1
            bx_low, bx_high = sorted((bx1, bx2))

        # vertical vs vertical
        if ax1 == ax2 and bx1 == bx2:
            if avx != bvx:
                return False
            return not (ay_high < by_low or by_high < ay_low)

        # horizontal vs horizontal
        if ay1 == ay2 and by1 == by2:
            if avy != bvy:
                return False
            return not (ax_high < bx_low or bx_high < ax_low)

        # vertical vs horizontal
        if ax1 == ax2:  # a vertical, b horizontal
            return bx_low <= avx <= bx_high and ay_low <= bvy <= ay_high
        else:  # a horizontal, b vertical
            return ax_low <= bvx <= ax_high and by_low <= avy <= by_high

    def rectangle_edges(x1, y1, x2, y2):
        min_x, max_x = sorted((x1, x2))
        min_y, max_y = sorted((y1, y2))
        return [
            ((min_x, min_y), (max_x, min_y)),
            ((max_x, min_y), (max_x, max_y)),
            ((max_x, max_y), (min_x, max_y)),
            ((min_x, max_y), (min_x, min_y)),
        ]

    # now that we have polygon, check biggest rectangle area
    red_points = set(grid)
    biggest_area = 0

    # a rectangle is defined by any two opposite red corners (axis-aligned)
    red_list = list(red_points)
    for i, (x1, y1) in enumerate(red_list):
        for x2, y2 in red_list[i + 1:]:
            if x1 == x2 or y1 == y2:
                continue  # need opposite corners, non-degenerate

            # four corners
            min_x, max_x = sorted((x1, x2))
            min_y, max_y = sorted((y1, y2))
            corners = [
                (min_x, min_y),
                (min_x, max_y),
                (max_x, min_y),
                (max_x, max_y),
            ]

            # all corners must be inside or on boundary
            if not all(point_inside(c) for c in corners):
                continue

            rect_edges = rectangle_edges(x1, y1, x2, y2)

            # rectangle edges cannot cross polygon edges (overlap on boundary is ok)
            crossing = False
            for re in rect_edges:
                for pe in edges:
                    if segments_intersect(re[0], re[1], pe[0], pe[1]):
                        # allow overlap: if both endpoints of rect edge on polygon edge, it's fine
                        if point_on_edge(re[0], pe) and point_on_edge(re[1], pe):
                            continue
                        # if they just touch at a corner that's on polygon edge, also fine
                        if point_on_edge(re[0], pe) or point_on_edge(re[1], pe):
                            continue
                        crossing = True
                        break
                if crossing:
                    break
            if crossing:
                continue

            min_x, max_x = sorted((x1, x2))
            min_y, max_y = sorted((y1, y2))
            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            if area <= biggest_area:
                continue
            biggest_area = area

    return biggest_area

def draw_grid(grid, points):
    max_x = max([point[0] for point in points])
    max_y = max([point[1] for point in points])

    for y in range(max_y+1):
        row = ''
        for x in range(max_x+1):
            if (x, y) in grid:
                row += '#'
            elif (x, y) in points:
                row += 'X'
            else:
                row += '.'
        print(row)
    
def main():
    print_markdown('day9/puzzle_1.md')
    biggest_possible = part1('day9/input.txt')
    print_solution(biggest_possible)

    print("\n\n\n")
    print_markdown('day9/puzzle_2.md')
    connecting_points = part2('day9/input.txt')
    print_solution(connecting_points)