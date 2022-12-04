import os, sys




def get_lines():
    with open("input4.txt", 'r') as f:
        return f.readlines()


def get_ordered_assignment(elves):
    lst = []

    for elf in elves:
        start, end = elf.split('-')
        start = int(start)
        end = int(end)

        lst.append([start, end])

    lst.sort(key = lambda x: (x[0], x[1]))

    return lst


def is_one_elf_capable(assignments):
    return (assignments[0][1] >= assignments[1][1]) \
            or (assignments[0][0] == assignments[1][0] and assignments[1][1] >= assignments[0][1])


def has_overlap(assignments):
    return (assignments[1][0] <= assignments[0][1])


def main():
    total = 0

    # read file
    lines = get_lines()

    for line in lines:
        line = line.strip()
        # 8-18,10-19
        elves_assgt = line.split(',')

        lst = get_ordered_assignment(elves_assgt)

        total += 1 if is_one_elf_capable(lst) else 0

    print(total)


def main_second():
    total = 0

    # read file
    lines = get_lines()

    for line in lines:
        line = line.strip()
        # 8-18,10-19
        elves_assgt = line.split(',')

        lst = get_ordered_assignment(elves_assgt)

        total += 1 if has_overlap(lst) else 0

    print(total)


if __name__ == "__main__":
    main()
    main_second()
