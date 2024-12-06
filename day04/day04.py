import sys
import numpy
from pprint import pprint



def puzzle1():
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    ans = 0

    north = [(0, 0), (-1, 0), (-2, 0), (-3, 0)]
    northeast = [(0, 0), (-1, 1), (-2, 2), (-3, 3)]
    east = [(0, 0), (0, 1), (0, 2), (0, 3)]
    southeast = [(0, 0), (1, 1), (2, 2), (3, 3)]
    south = [(0, 0), (1, 0), (2, 0), (3, 0)]
    southwest = [(0, 0), (1, -1), (2, -2), (3, -3)]
    west = [(0, 0), (0, -1), (0, -2), (0, -3)]
    northwest = [(0, 0), (-1, -1), (-2, -2), (-3, -3)]

    board = data.split('\n')
    x_positions = [(j, i) for j in range(len(board[0])) for i in range(len(board)) if board[i][j] == 'X']
    m_positions = [(j, i) for j in range(len(board[0])) for i in range(len(board)) if board[i][j] == 'M']
    a_positions = [(j, i) for j in range(len(board[0])) for i in range(len(board)) if board[i][j] == 'A']
    s_positions = [(j, i) for j in range(len(board[0])) for i in range(len(board)) if board[i][j] == 'S']

    for pos in x_positions:
        n = list(map(lambda l: numpy.add(pos, l), north))
        ne = list(map(lambda l: numpy.add(pos, l), northeast))
        e = list(map(lambda l: numpy.add(pos, l), east))
        se = list(map(lambda l: numpy.add(pos, l), southeast))
        s = list(map(lambda l: numpy.add(pos, l), south))
        sw = list(map(lambda l: numpy.add(pos, l), southwest))
        w = list(map(lambda l: numpy.add(pos, l), west))
        nw = list(map(lambda l: numpy.add(pos, l), northwest))
        positions = [n, ne, e, se, s, sw, w, nw]
        def in_bounds(x):
            for tup in x:
                if not 0 <= tup[0] <= len(board) or not 0 <= tup[1] <= len(board[0]):
                    return False
            return True
        valid_positions = list(filter(in_bounds, positions))
        for v in valid_positions:
            v = list(map(tuple, v))
            if v[0] in x_positions and v[1] in m_positions and v[2] in a_positions and v[3] in s_positions:
                ans += 1

    print(f'The answer to puzzle 1 is {ans}')



def puzzle2():
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    ans = 0

    corners = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    board = data.split('\n')
    def in_bounds(x):
        for tup in x:
            if not 0 <= tup[0] < len(board) or not 0 <= tup[1] < len(board[0]):
                return False
        return True
    def valid(x):
        c1, c2, c3, c4 = x
        if board[c1[0]][c1[1]] == 'M' and board[c2[0]][c2[1]] == 'M' and board[c3[0]][c3[1]] == 'S' and board[c4[0]][c4[1]] == 'S':
            return True
        if board[c1[0]][c1[1]] == 'S' and board[c2[0]][c2[1]] == 'M' and board[c3[0]][c3[1]] == 'M' and board[c4[0]][c4[1]] == 'S':
            return True
        if board[c1[0]][c1[1]] == 'S' and board[c2[0]][c2[1]] == 'S' and board[c3[0]][c3[1]] == 'M' and board[c4[0]][c4[1]] == 'M':
            return True
        if board[c1[0]][c1[1]] == 'M' and board[c2[0]][c2[1]] == 'S' and board[c3[0]][c3[1]] == 'S' and board[c4[0]][c4[1]] == 'M':
            return True
        return False

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'A':
                c = list(map(lambda l: numpy.add((i, j), l), corners))
                if in_bounds(c) and valid(c):
                    print(f'Position {i}, {j} is valid.')
                    ans += 1

    print(f'The answer to puzzle 2 is {ans}.')



if __name__ == '__main__':
    puzzle1()
    puzzle2()