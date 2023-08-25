# BRUTE
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        change = []
        n,m = len(matrix),len(matrix[0])

        for r in range(n) :
            for c in range(m) :
                if matrix[r][c] == 0 :
                    change.append([r,c])
        
        for row,col in change :
            for i in range(m) :
                matrix[row][i] = 0
            for i in range(n) :
                matrix[i][col] = 0
        
        return matrix

        #SC -> O(n^2)

#BETTER
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols = len(matrix),len(matrix[0])
        row_mark,col_mark = [0]*rows,[0]*cols
        for r in range(rows) :
            for c in range(cols) :
                if matrix[r][c] == 0 :
                    row_mark[r] = 1
                    col_mark[c] = 1
        for r in range(rows) :
            for c in range(cols) :
                if row_mark[r] == 1 or col_mark[c] == 1 :
                    matrix[r][c] = 0

        #SC -> O(2N)

#Optimal
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols = len(matrix),len(matrix[0])
        #row_mark,col_mark = [0]*rows,[0]*cols
        #use matrix[..][0] for rows
        #use matrix[0][..] for cols
        cols0 = 1
        for r in range(rows) :
            for c in range(cols) :
                if matrix[r][c] == 0 :
                    matrix[r][0] = 0
                    if c != 0 :
                        matrix[0][c] = 0
                    else :
                        cols0 = 0
                    
        for r in range(1,rows) :
            for c in range(1,cols) :
                if matrix[r][c] != 0 :
                    if matrix[r][0] == 0  or matrix[0][c] == 0 :
                        matrix[r][c] = 0
        
        if matrix[0][0] == 0 :
            for c in range(cols) :
                matrix[0][c] = 0 
        if cols0 == 0 :
            for r in range(rows) :
                matrix[r][0] = 0

        #SC -> O(1)