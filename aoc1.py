


if __name__ == "__main__":
    # read file
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
                local = 0

    print( max_cal )

