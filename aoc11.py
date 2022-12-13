from collections import deque, defaultdict
import pprint
import heapq
import math

PP = pprint.PrettyPrinter(indent=4)


def get_lines():
    with open("input11.txt", 'r') as f:
        return f.readlines()


def set_up(lines):
    data = {}

    for i in range(0, len(lines), 7):
        monkey = lines[i].strip()[:-1].split()
        items = lines[i+1].strip().split(': ')[-1]
        items = deque(list(map(int, items.split(', '))))
        operation_x = lines[i+2].strip().split(': ')[-1].split('=')[-1].split()
        # operation = operation_x.split('=').strip().split()
        test = int(lines[i+3].strip().split(': ')[-1].split()[-1])
        if_true = lines[i+4].strip().split(': ')[-1].split()[-1]
        if_false = lines[i+5].strip().split(': ')[-1].split()[-1]

        data[monkey[-1]] = {
            'items': items,
            'operation': operation_x,
            'test': test,
            'if_true': if_true,
            'if_false': if_false
        }

    # PP.pprint(data)
    return data


def parse_operation(op, v):
    x = v

    if op[1] == '+':
        x += int(op[2]) if op[2] != 'old' else x
    elif op[1] == '*':
        x *= int(op[2]) if op[2] != 'old' else x
    elif op[1] == '-':
        x -= int(op[2]) if op[2] != 'old' else x
    elif op[1] == '*':
        x /= int(op[2]) if op[2] != 'old' else x

    return x


def get_lcm(monkeys):
    x = 1

    for v in monkeys.values():
        x *= v.get('test')

    return x


def main(rounds=20):
    monkeys = set_up(get_lines())
    inspections = [0 for _ in range(len(monkeys))]

    lcm = get_lcm(monkeys)

    for i in range(rounds):

        for monkey in range(len(monkeys)):
            idx = str(monkey)

            items = monkeys[idx].get('items')

            while items:
                val = items.popleft()
                inspections[monkey] -= 1
                new_val = parse_operation(monkeys[idx].get('operation'), val)
                if rounds == 20:
                    new_val //= 3
                else:
                    new_val = new_val % lcm

                if new_val % monkeys[idx].get('test') == 0:
                    monkeys[monkeys[idx].get('if_true')].get('items').append(new_val)
                else:
                    monkeys[monkeys[idx].get('if_false')].get('items').append(new_val)

        # print("\n############")
        # print(f"Round {i}")
        # PP.pprint(monkeys)

    heapq.heapify(inspections)

    print(-heapq.heappop(inspections) * -heapq.heappop(inspections))


if __name__ == "__main__":
    # main()
    print ("\n###################################\n")
    main(rounds=10000)
