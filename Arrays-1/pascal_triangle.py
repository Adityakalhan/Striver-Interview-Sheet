class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1 :
            return [[1]]
        if numRows == 1 :
            return [[1],[1,1]]
        
        pascalsTriangle = [[1],[1,1]]

        for row in range(2,numRows) :
            pascalsTriangle.append([1])
            for i in range(1,row) :
                pascalsTriangle[row].append( pascalsTriangle[row-1][i-1] + pascalsTriangle[row-1][i] )
            pascalsTriangle[row].append(1)
        return pascalsTriangle