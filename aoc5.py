import os, sys
from collections import deque


class Stacks(object):

    def __init__(self):
        self.crates = []

        # manually fill
        self.init()


    def init(self):
        lists = [
            ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
            ['M', 'Q', 'H'],
            ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
            ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
            ['M', 'T', 'H', 'P'],
            ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
            ['M', 'N', 'B', 'F', 'V', 'R'],
            ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
            ['P', 'D', 'B', 'C', 'N']
        ]

        for lst in lists:
            self.crates.append(deque(lst))

    
    # the input in 1-based, so adjust the from to, to be 0 based
    def move(self, amt, frm, to):
        f, t = frm -1, to -1
        q = amt

        while self.crates[f] and q:
            self.crates[t].append(self.crates[f].pop())
            q -= 1

    def move_bulk(self, amt, frm, to):
        f, t = frm -1, to -1
        q = amt
        tmp = []

        while self.crates[f] and q:
            tmp.append(self.crates[f].pop())
            q -= 1

        self.crates[t].extend(tmp[::-1])


    def peek_top(self):
        top_str = []

        for crate in self.crates:
            if crate:
                top_str.append(crate[-1])
            else:
                top_str.append(" ")

        return "".join(top_str)

            

def get_lines():
    with open("input5.txt", 'r') as f:
        return f.readlines()


def main():
    top = None
    # read file
    lines = get_lines()
    stacks = Stacks()
    stacks_2 = Stacks()

    for line in lines:
        line = line.strip()
        # move <amt> from <frm> to <to>
        cmds = line.split(' ')
        qty = int(cmds[1])
        frm = int(cmds[3])
        to = int(cmds[5])

        stacks.move(qty, frm, to)
        stacks_2.move_bulk(qty, frm, to)

    print(stacks.peek_top())
    print(stacks_2.peek_top())


if __name__ == "__main__":
    main()
