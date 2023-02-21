class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        ls=""
        for i in licensePlate:
            if i.isalpha():
                i=i.lower()
                ls+=i

        lst=[]
        count=0
        lss=ls
        for i in words:
            for j in lss:
                if j in i:
                    count+=1
                else:
                    break

            if len(i)==count:
                lst.append(i)
            count=0

        
        nimadur=lst[0]

        for i in lst:
            if len(i)<len(nimadur):
                nimadur=i
        
        return nimadur
    
asdf=Solution()
print(asdf.shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"]))