import os, sys
import pprint

from collections import deque
import heapq

PP = pprint.PrettyPrinter(indent=4)
FILE_SYSTEM = {}
HEAP = []

LIMIT = 70000000
NEEDED = 30000000


def get_lines():
    with open("input7.txt", 'r') as f:
        return f.readlines()


def init_system():
    FILE_SYSTEM['/'] = {}
    curr_loc = None
    stack = deque()

    # read file
    lines = get_lines()
    curr_d = FILE_SYSTEM
    ls_flag = False

    for line in lines:
        # 2 types of input, commands and system reponse
        line = line.strip()
        parts = line.split()

        if ls_flag and parts[0] != '$':
            if parts[0] == 'dir':
                curr_d[parts[1]] = {}
            else:
                size = int(parts[0])
                curr_d[parts[1]] = size


        if parts[0] == '$':
            if ls_flag: ls_flag = False

            if parts[1] == 'cd':
                if parts[2] == '..':
                    curr_loc, curr_d = stack.pop()
                else:
                    if curr_loc:
                        stack.append((curr_loc, curr_d))

                    curr_loc = parts[2]
                    curr_d = curr_d[curr_loc]
            elif parts[1] == 'ls':
                ls_flag = True


def graph_traversal_at_most_100k(curr):
    local_total, local_amt = 0, 0

    for k, v in curr.items():
        if isinstance(v, dict):
            total, amt = graph_traversal_at_most_100k(v)
            local_total += total
            local_amt += amt
        else:
            local_total += v

    if local_total <= 100000:
        local_amt += local_total

    heapq.heappush(HEAP, local_total)

    return local_total, local_amt
            


def main():
    init_system()
    # PP.pprint(FILE_SYSTEM)
    amt = 0

    total, amt = graph_traversal_at_most_100k(FILE_SYSTEM.get('/'))
    print(amt)

    diff = LIMIT - total

    if diff >= NEEDED:
        print("we are good")
    else:
        x = heapq.heappop(HEAP)

        while (x + diff) < NEEDED:
            x = heapq.heappop(HEAP)

        print(x)


if __name__ == "__main__":
    main()
