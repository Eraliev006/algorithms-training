

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""



def isValidSudoku(board: List[List[str]]) -> bool:
    from collections import defaultdict
    rows = defaultdict(set)
    colums = defaultdict(set)
    squares = defaultdict(set)

    for r in range(len(board)):
        for c in range(len(board[r])):
            val = board[r][c]

            if val == ".":
                continue
            
            if val in rows[r] or val in colums[c] or val in squares[(r // 3, c // 3)]:
                return False

            rows[r].add(val)
            colums[c].add(val)
            squares[(r // 3, c // 3)].add(val)

    return True