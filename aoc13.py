import pprint
import json


PP = pprint.PrettyPrinter(indent=4)


def get_lines():
    with open("input13.txt", 'r') as f:
        return f.readlines()


def is_in_order(left, right):
    
    i, j = 0, 0
    while i < len(left) and j < len(right):

        if isinstance(left[i], int) and isinstance(right[j], int):
            if left[i] < right[j]:
                return True
            elif left[i] > right[j]:
                return False
        elif isinstance(left[i], list) and isinstance(right[j], list):
            x = is_in_order(left[i], right[j])
            if x is not None: return x
        else:
            tmp1, tmp2 = None, None
            if isinstance(left[i], int):
                tmp1 = [left[i]]
                tmp2 = right[j]
            elif isinstance(right[j], int):
                tmp1 = left[i]
                tmp2 = [right[j]]

            x = is_in_order(tmp1, tmp2)
            if x is not None: return x

        i += 1; j += 1
        
    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False

    return None


def main():
    lines = get_lines()
    pair = 0
    total = 0

    for i in range(0, len(lines), 3):
        left = json.loads(lines[i])
        right = json.loads(lines[i+1])

        pair += 1
        if is_in_order(left, right):
            total += pair

    print(total)


def merge(arr, l, m ,r):
    n1, n2 = m - l + 1, r - m

    temp_l = [None] * n1
    temp_r = [None] * n2

    for i in range(n1):
        temp_l[i] = arr[l+i]
    for j in range(n2):
        temp_r[j] = arr[m+j+1]

    i, j, k = 0, 0, l

    while i < n1 and j < n2:
        if is_in_order(temp_l[i], temp_r[j]):
            arr[k] = temp_l[i]
            i += 1
        else:
            arr[k] = temp_r[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = temp_l[i]
        i += 1; k += 1

    while j < n2:
        arr[k] = temp_r[j]
        j += 1; k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r-l) // 2

        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)


def main2():
    lines = get_lines()
    total = 1
    full_arr = []

    for i in range(0, len(lines), 3):
        left = json.loads(lines[i])
        right = json.loads(lines[i+1])

        full_arr.append(left)
        full_arr.append(right)

    full_arr.append([[2]])
    full_arr.append([[6]])

    merge_sort(full_arr, 0, len(full_arr)-1)

    for i, x in enumerate(full_arr):
        s = json.dumps(x)

        if s == "[[2]]" or s == "[[6]]":
            total *= (i+1)

    print(total)


if __name__ == "__main__":
    main()
    # print ("\n###################################\n")
    main2()
