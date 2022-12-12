from collections import deque
import pprint


PP = pprint.PrettyPrinter(indent=4)

class Planck(object):
    U = [0, 1]
    D = [0, -1]
    R = [1, 0]
    L = [-1, 0]
    START = [0, 0]
    DIR_MAPPING = {'R': R, 'L': L, 'U': U, 'D': D}


    def __init__(self, lines):
        self._head = self.START
        self._tails = [self.START for _ in range(9)]
        # self._tails = [self.START]
        self._visited = set(tuple(self.START))

        self._process_lines(lines)

    def _is_touching(self, head, tail):
        # greater than 1 on up, down, left, right, or diagonal is not touching
        return abs(head[0] - tail[0]) <= 1 \
                and abs(head[1] - tail[1]) <= 1

    def _move_tail(self, head, tail, is_last=False):
        # x-axis difference, catch up on that axis
        if head[0] - tail[0] >= 1 and head[1] - tail[1] == 0:
            tail = [sum(x) for x in zip(tail, [1, 0])]
        elif head[0] - tail[0] <= 1 and head[1] - tail[1] == 0:
            tail = [sum(x) for x in zip(tail, [-1, 0])]
        elif head[0] - tail[0] == 0 and head[1] - tail[1] >= 1:
            tail = [sum(x) for x in zip(tail, [0, 1])]
        elif head[0] - tail[0] == 0 and head[1] - tail[1] <= 1:
            tail = [sum(x) for x in zip(tail, [0, -1])]
        else: # diagonal
            # both positives, q1, moves 1, 1
            if head[0] - tail[0] > 0 and head[1] - tail[1] > 0:
                tail = [sum(x) for x in zip(tail, [1, 1])]
            # pos, neg, q4, moves 1, -1
            elif head[0] - tail[0] > 0 and head[1] - tail[1] < 0:
                tail = [sum(x) for x in zip(tail, [1, -1])]
            # neg, pos, q2, moves -1, 1
            elif head[0] - tail[0] < 0 and head[1] - tail[1] > 0:
                tail = [sum(x) for x in zip(tail, [-1, 1])]
            # neg, neg, q2, moves -1, -1
            else:
                tail = [sum(x) for x in zip(tail, [-1, -1])]

        if is_last: 
            self._visited.add(tuple(tail))

        return tail


    def _process_lines(self, lines):
        
        for line in lines:
            line = line.strip()
            dir, qty = line.split()

            # displace head 
            for _ in range(int(qty)):
                self._head = [sum(x) for x in zip(self._head, self.DIR_MAPPING[dir])]
                head = self._head
                # print(f"head location {head}")
                for idx, tail in enumerate(self._tails):
                    # print(f"tail location {tail}")
                    if not self._is_touching(head, tail):
                        self._tails[idx] = self._move_tail(head, tail, is_last=idx==len(self._tails)-1)
                    head = tail

    def tail_visit_n(self):
        return len(self._visited)



def get_lines():
    with open("input9.txt", 'r') as f:
        return f.readlines()


def main():
    lines = get_lines()
    planck_sim = Planck(lines)

    print(planck_sim.tail_visit_n())


if __name__ == "__main__":
    main()
