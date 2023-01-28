class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zipp=zip(*matrix)
        for i, j in enumerate(zipp):
            matrix[i]=reversed(j)