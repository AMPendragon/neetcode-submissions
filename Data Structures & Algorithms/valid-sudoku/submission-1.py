class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            col = [board[x][i] for x in range(9)]
            row_seen = set()
            col_seen = set()
            for n in row:
                if n not in row_seen:
                    row_seen.add(n)
                elif n != '.':
                    return False
            for n in col:
                if n not in col_seen:
                    col_seen.add(n)
                elif n != '.':
                    return False

        for i in range(3):
            for j in range(3):
                box = [board[x][j*3:j*3+3] for x in range(i*3,i*3+3)]
                flatten = [n for x in box for n in x]
                seen = set()
                for n in flatten:
                    if n not in seen:
                        seen.add(n)
                    elif n != '.':
                        return False

        return True