class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        if "".join(word1)=="".join(word2):
            return True
        return False

