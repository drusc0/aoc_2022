import heapq


if __name__ == "__main__":
    # read file
    _max_arr = []
    with open("input1.txt", 'r') as f:
        max_cal = 0
        local = 0

        while True:
            line = f.readline()
            if not line: break

            line = line.strip()
            if line != "":
                local += int(line)
                max_cal = max(max_cal, local)
            else:
                heapq.heappush(_max_arr, -max_cal)
                max_cal = 0
                local = 0

    total = sum([-heapq.heappop(_max_arr) for _ in range(3)])

    print( total )

