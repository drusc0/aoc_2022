import os, sys
import string
from collections import Counter


MAPPING = {v: i+1 for i, v in enumerate(list(string.ascii_letters))}


def get_lines():
    with open("input3.txt", 'r') as f:
        return f.readlines()


def main_second():
    total = 0

    # read file
    lines = get_lines()
    
    for i in range(0, len(lines), 3):
        line1, line2, line3 = lines[i].strip(), lines[i+1].strip(),lines[i+2].strip()
        counter1, counter2, counter3 = Counter(line1), Counter(line2), Counter(line3)

        intersection = counter1 & counter2 & counter3
        
        if intersection:
            val = list(intersection.keys())[0]
            total += MAPPING.get(val)

    print(total)


def main():
    total = 0

    # read file
    lines = get_lines()

    for line in lines:
        line = line.strip()
        size = len(line)
        counter1, counter2 = Counter(line[:size//2]), Counter(line[size//2:])

        intersection = counter1 & counter2
            
        if intersection:
            val = list(intersection.keys())[0]
            total += MAPPING.get(val)

    print(total)


if __name__ == "__main__":
    main()
    main_second()
