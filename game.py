import sys

# initial sudoku matrix
V = [
    0, 0, 0, 2, 6, 0, 7, 0, 1,
    6, 8, 0, 0, 7, 0, 0, 9, 0,
    1, 9, 0, 0, 0, 4, 5, 0, 0,
    8, 2, 0, 1, 0, 0, 0, 4, 0,
    0, 0, 4, 6, 0, 2, 9, 0, 0,
    0, 5, 0, 0, 0, 3, 0, 2, 8,
    0, 0, 9, 3, 0, 0, 0, 7, 4,
    0, 4, 0, 0, 5, 0, 0, 3, 6,
    7, 0, 3, 0, 1, 8, 0, 0, 0
]
V1=[ 8,0,0,0,0,0,0,0,0,
    0,0,3,6,0,0,0,0,0,
    0,7,0,0,9,0,2,0,0,
    0,5,0,0,0,7,0,0,0,
    0,0,0,0,4,5,7,0,0,
    0,0,0,1,0,0,0,3,0,
    0,0,1,0,0,0,0,6,8,
    0,0,8,5,0,0,0,1,0,
    0,9,0,0,0,0,4,0,0]

# fill matrix using recursive backtracking
# `fw` stands for forward and `bw` for backward
def fill_matrix(V, ignore_pos, i=0, direction='fw'):
    if i > 80:
        return True

    if i in ignore_pos:
        if direction == 'fw':
            fill_matrix(V, ignore_pos, i + 1)
        else:
            fill_matrix(V, ignore_pos, i - 1, 'bw')
    elif V[i] < 9:
        if has_violation(V, V[i] + 1, i):
            V[i] += 1
            fill_matrix(V, ignore_pos, i)
        else:
            V[i] += 1
            fill_matrix(V, ignore_pos, i + 1)
    else:
        V[i] = 0
        fill_matrix(V, ignore_pos, i - 1, 'bw')


# get positions for previously populated values
def set_ignore_pos_array(V):
    ignore_pos = []

    for index, value in enumerate(V):
        if value != 0:
            ignore_pos.append(index)

    return ignore_pos


# given an index, get all of its crossing positions
def get_positions_to_check(V, i):
    positions_to_check = [i]
    before_up = i - 9
    after_down = i + 9
    before_left = i
    after_right = i + 1

    if i >= 0 and i <= 80:
        while before_up >= 0:
            positions_to_check.append(before_up)
            before_up -= 9

        while after_down <= 80:
            positions_to_check.append(after_down)
            after_down += 9

        while before_left % 9 != 0:
            before_left -= 1
            positions_to_check.append(before_left)

        while after_right % 9 != 0:
            positions_to_check.append(after_right)
            after_right += 1

        return positions_to_check


# check for violations when inserting a value in a given position
def has_violation(V, value, index):
    pos_to_check = get_positions_to_check(V, index)

    if pos_to_check:
        for i in pos_to_check:
            if V[i] == value:
                return True
        return False
    else:
        return "No index available."


def main():
    # Increase recursion limit due to no TRE in Python
    sys.setrecursionlimit(100000)

    ignore_pos = set_ignore_pos_array(V)

    fill_matrix(V, ignore_pos)

    # solved sudoku matrix
    for i in range(len(V)):

        if i%9==0 and i>=9:
            print("\n")
        print(V[i], " ", end="")


if __name__ == "__main__": main()

# solved sudoku matrix
'''
4, 3, 5, 2, 6, 9, 7, 8, 1,
6, 8, 2, 5, 7, 1, 4, 9, 3,
1, 9, 7, 8, 3, 4, 5, 6, 2,
8, 2, 6, 1, 9, 5, 3, 4, 7,
3, 7, 4, 6, 8, 2, 9, 1, 5,
9, 5, 1, 7, 4, 3, 6, 2, 8,
5, 1, 9, 3, 2, 6, 8, 7, 4,
2, 4, 8, 9, 5, 7, 1, 3, 6,
7, 6, 3, 4, 1, 8, 2, 5, 9
'''
