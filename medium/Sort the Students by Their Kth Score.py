class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)

sp=Solution()
print(sp.sortTheStudents([[1, 2, 3, 4], [4, 3, 2, 1], [4, 5, 6, 7]], 2))