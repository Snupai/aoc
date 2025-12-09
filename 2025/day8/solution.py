from helper.markdown_printer import print_markdown, print_solution
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure.
    Reference: https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True
    
    def get_circuit_sizes(self):
        roots = set()
        for i in range(len(self.parent)):
            root = self.find(i)
            roots.add(root)
        
        sizes = [self.size[root] for root in roots]
        return sizes
    
    def is_all_connected(self):
        roots = set()
        for i in range(len(self.parent)):
            roots.add(self.find(i))
        return len(roots) == 1

def part1(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().strip()
    
    junction_boxes = []
    for line in input_data.split('\n'):
        if not line.strip():
            continue
        x, y, z = map(int, line.split(','))
        junction_boxes.append((x, y, z))
    
    n = len(junction_boxes)
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(junction_boxes[i], junction_boxes[j])
            edges.append((distance, i, j))
    
    edges.sort()
    
    uf = UnionFind(n)
    pairs_tried = 0
    
    for distance, i, j in edges:
        if pairs_tried >= 1000:
            break
        
        pairs_tried += 1
        uf.union(i, j)
    
    circuit_sizes = uf.get_circuit_sizes()
    circuit_sizes.sort(reverse=True)
    
    if len(circuit_sizes) < 3:
        result = 1
        for size in circuit_sizes:
            result *= size
    else:
        result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    
    return result

def part2(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().strip()
    
    junction_boxes = []
    for line in input_data.split('\n'):
        if not line.strip():
            continue
        x, y, z = map(int, line.split(','))
        junction_boxes.append((x, y, z))
    
    n = len(junction_boxes)
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(junction_boxes[i], junction_boxes[j])
            edges.append((distance, i, j))
    
    edges.sort()
    
    uf = UnionFind(n)
    last_connection = None
    
    for distance, i, j in edges:
        if uf.union(i, j):
            last_connection = (i, j)
            
            if uf.is_all_connected():
                break
    
    if last_connection:
        i, j = last_connection
        result = junction_boxes[i][0] * junction_boxes[j][0]
        return result
    else:
        return 0

def main():
    print_markdown('day8/puzzle_1.md')
    result = part1('day8/input.txt')
    print_solution(result)
    
    print("\n\n\n")
    
    print_markdown('day8/puzzle_2.md')
    result = part2('day8/input.txt')
    print_solution(result)