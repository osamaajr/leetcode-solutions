class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            seen = set()
            for value in row:
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)

        for box_col in range(0,9,3):
            for box_row in range(0,9,3):
                seen = set()
                for square_col in range(box_col, box_col+3):
                    for square_row in range(box_row, box_row+3):
                        value = board[square_row][square_col]
                        if value == ".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value)
        
        return True