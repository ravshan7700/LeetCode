class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dct={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9": "wxyz" 
        }
        lst=[]
        for i in digits:
            if i in dct.keys():
                lst.append(dct[i])
        
        


sp=Solution()
print(sp.letterCombinations("23"))
                
