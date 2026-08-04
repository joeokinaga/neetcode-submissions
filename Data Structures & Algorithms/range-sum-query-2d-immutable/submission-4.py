class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr = []
        for i in range(len(matrix)):
            arr2 = []
            prefix = 0
            for j in range(len(matrix[0])):
                prefix += matrix[i][j]
                arr2.append(prefix)

            self.arr.append(arr2)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            if col1 == 0:
                sum += self.arr[i][col2]
                continue
            sum = sum + (self.arr[i][col2] - self.arr[i][col1-1])

        return sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)