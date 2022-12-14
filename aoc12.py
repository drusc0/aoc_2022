from collections import deque
import pprint


PP = pprint.PrettyPrinter(indent=4)


def get_lines():
    with open("input12.txt", 'r') as f:
        return f.readlines()


def set_up(lines):
    mat = []
    
    for line in lines:
        mat.append(list(line.strip()))

    return mat


def get_location(matrix, char_loc):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == char_loc:
                return r, c
    
    return -1, -1


def is_valid(matrix, seen, r, c, cur):
    return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[0]) and not seen[r][c] \
        and (ord(matrix[r][c]) - ord(cur) <= 1 or ord(matrix[r][c]) - ord(cur) == 25)


def bfs(matrix, s_r, s_c, e_r, e_c):
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    q = deque()
    q.append((s_r, s_c, 0))
    visited[s_r][s_c] = True

    while q:
        r, c, d = q.popleft()

        if r == e_r and c == e_c:
            return d

        # top
        if is_valid(matrix, visited, r-1, c, matrix[r][c]):
            visited[r-1][c] = True
            q.append((r-1, c, d+1))

        # bottom
        if is_valid(matrix, visited, r+1, c, matrix[r][c]):
            visited[r+1][c] = True
            q.append((r+1, c, d+1))
            
        # left
        if is_valid(matrix, visited, r, c-1, matrix[r][c]):
            visited[r][c-1] = True
            q.append((r, c-1, d+1))
            
        # right
        if is_valid(matrix, visited, r, c+1, matrix[r][c]):
            visited[r][c+1] = True
            q.append((r, c+1, d+1))

    return float('inf')


def main(start='S', end='E'):
    matrix = set_up(get_lines())

    s_r, s_c = get_location(matrix, start)
    e_r, e_c = get_location(matrix, end)

    matrix[s_r][s_c] = 'a'
    matrix[e_r][e_c] = 'z'

    print(bfs(matrix, s_r, s_c, e_r, e_c))

def main2():
    matrix = set_up(get_lines())

    s_r, s_c = get_location(matrix, 'S')
    e_r, e_c = get_location(matrix, 'E')
    matrix[s_r][s_c] = 'a'
    matrix[e_r][e_c] = 'z'

    _min = float('inf')
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 'a':
                _min = min(_min, bfs(matrix, r, c, e_r, e_c))

    print(_min)


if __name__ == "__main__":
    main()
    print ("\n###################################\n")
    main2()
