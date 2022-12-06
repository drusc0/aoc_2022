import os, sys
from collections import defaultdict

# 2 pointers to address the beginning and end, keep a dictionary with a single item for each item.
def sliding_window(packet, lim=4):
    a, z = 0, 0
    d = defaultdict(int)

    while z < len(packet):

        d[packet[z]] += 1

        while d[packet[z]] > 1:
            d[packet[a]]-= 1
            a += 1

        z += 1
        if z-a == lim:
            break

    print(z)
            

def get_lines():
    with open("input6.txt", 'r') as f:
        return f.readlines()


def main():
    top = None
    # read file
    lines = get_lines()

    for line in lines:
        # should only be one line, but we will do it this way just in case
        line = line.strip()
        sliding_window(line)
        sliding_window(line, 14)


if __name__ == "__main__":
    main()
