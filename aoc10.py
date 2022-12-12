from collections import deque
import pprint


PP = pprint.PrettyPrinter(indent=4)


def get_lines():
    with open("input10.txt", 'r') as f:
        return f.readlines()


def main():
    steps = deque([20, 60, 100, 140, 180, 220])
    step = steps.popleft()
    total_strength = 0
    ticks = 0
    x = 1

    for idx, line in enumerate(get_lines()):
        line = line.strip()
        cmd = line.split()

        if len(cmd) == 1:
            ticks += 1
        else:
            ticks += 2
            x += int(cmd[1])

        if ticks + 1 == step or ticks + 2 == step:
            # print(f"ticks {ticks} step {step} X {x} line {line} - {idx}")
            total_strength += x * step
            if steps:
                step = steps.popleft()
            else:
                break

    print(total_strength)


def main2():
    deq = deque(get_lines())
    msg = [['.' for _ in range(40)] for _ in range(6)]
    row, idx, counter = 0, 0, 0
    current_row = msg[row]

    ticks = 0
    x = 1
    cmd = None

    while True:
        ticks += 1

        if counter == 0:
            cmd = deq.popleft().strip().split()

        
        # draw the lit item in row
        if idx == x or idx == x + 1 or idx == x - 1:
            current_row[idx] = '#'
        idx += 1
        

        if ticks % 40 == 0:
            # print(f"\t\ttick: {ticks} | X: {x}")
            row += 1
            idx = 0
            if row == 6: break
            current_row = msg[row]


        if counter == 0 and len(cmd) == 2:
            counter += 1
        elif counter == 1:
            counter = 0
            x += int(cmd[1])


    print ("\n")
    for m in msg:
        print("".join(m))


if __name__ == "__main__":
    main()
    print ("\n###################################\n")
    main2()
