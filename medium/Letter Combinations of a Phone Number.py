class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dct={
            "abc": "2",
            "def": "3",
            "ghi": "4",
            "jkl": "5",
            "mno": "6",
            "pqrs": "7",
            "tuv": "8",
            "wxyz": "9"
        }

        lst=dct.values()
        lst2=digits.split()



        
        return lst

sp=Solution()
print(sp.letterCombinations("33"))
                
