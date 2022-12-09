import os, sys
from collections import deque
import pprint


PP = pprint.PrettyPrinter(indent=4)


def get_lines():
    with open("input8.txt", 'r') as f:
        return f.readlines()


def init_matrix(inp):
    return [[int(x) for x in line.strip()] for line in inp]


def find_score(mat, r, c, v):
    top_local, bottom_local, left_local, right_local = 0, 0, 0, 0
    scenic_score = 0

    # iterate left
    j = c-1
    while j >= 0:
        left_local += 1
        if mat[r][j] >= v:
            break
        j -= 1

    # iterate right
    j = c+1
    while j < len(mat):
        right_local += 1
        if mat[r][j] >= v:
            break
        j += 1

    # iterate top
    i = r-1
    while i >= 0:
        top_local += 1
        if mat[i][c] >= v:
            break
        i -= 1

    # iterate bottom
    i = r+1
    while i < len(mat[r]):
        bottom_local += 1
        if mat[i][c] >= v:
            break
        i += 1

    scenic_score = top_local * bottom_local * left_local * right_local

    return scenic_score


def is_visible(mat, r, c, v):
    top, bottom, left, right = True, True, True, True

    # iterate left
    j = c-1
    while j >= 0:
        if mat[r][j] >= v:
            left = False
            break
        j -= 1

    # iterate right
    j = c+1
    while j < len(mat):
        if mat[r][j] >= v:
            right = False
            break
        j += 1

    # iterate top
    i = r-1
    while i >= 0:
        if mat[i][c] >= v:
            top = False
            break
        i -= 1

    # iterate bottom
    i = r+1
    while i < len(mat[r]):
        if mat[i][c] >= v:
            bottom = False
            break
        i += 1

    return top or bottom or left or right


def main():
    max_view = 0
    total = 0
    # read file and create matrix
    mat = init_matrix(get_lines())
    # perimeter and deduct the 4 corners that are being accounted for twice
    total += len(mat) * 2 + len(mat[0]) * 2 - 4

    for i, row in enumerate(mat):
        if i == 0 or i == len(mat)-1: continue

        for j, cell_v in enumerate(row):
            if j == 0 or j == len(mat[i])-1: continue

            if is_visible(mat, i, j, cell_v):
                total += 1
            max_view = max(max_view, find_score(mat, i, j, cell_v))

    print(total, max_view)


if __name__ == "__main__":
    main()
