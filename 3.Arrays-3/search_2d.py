class Solution:
    def __binarySearch(self,arr,target) :
        lo,hi = 0,len(arr)-1
        while lo <= hi :
            mid = (lo +hi)//2
            if arr[mid] == target :
                return True
            if arr[mid] > target :
                hi = mid - 1
            else :
                lo = mid + 1
        return False
    def __getRow(self,matrix,target) :
        lo,hi = 0,len(matrix)-1
        while lo <= hi :
            mid = (lo + hi)//2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target :
                return mid
            if matrix[mid][0] >= target :
                hi = mid - 1
            else :
                lo = mid + 1
        return -1


    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = self.__getRow(matrix,target)
        return self.__binarySearch(matrix[row],target) if row != -1 else False