class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=len(board)
        col=len(board[0])
        for i in range(row):
            for j in range(col):
                check= board[i][j]
                if check=='.':
                    continue
                if self.check_rows(board, i, j, check, col) is False or self.check_cols(board, i, j, check, row) is False or self.check_box(board, i, j, check) is False:
                    return False
        return True

            



    def check_rows(self, board, row_num, col_num, check, col):   
        for j in range(col):
            if j==col_num or board[row_num][j]=='.':
                continue
            elif board[row_num][j]==check:
                return False
        
        return True

    def check_cols(self, board, row_num, col_num, check, row):   
        for i in range(row):
            if i==row_num or board[i][col_num]=='.':
                continue
            elif board[i][col_num]==check:
                return False
        
        return True

    def check_box(self, matrix, row_num, col_num, check):   
        row_quotient=row_num//3 #0,1,2
        col_quotient=col_num//3 #0,1,2
        for m in range(3):
            for n in range(3):
                i=3*row_quotient+m
                j=3*col_quotient+n
                if (i==row_num and j==col_num) or matrix[i][j]=='.':
                    continue
                elif matrix[i][j]==check:
                    return False
        return True
            
        