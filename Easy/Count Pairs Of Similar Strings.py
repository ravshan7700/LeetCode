class Solution:
    def similarPairs(self, words: list[str]) -> int:
        lst=[]
    
        count=0
        cheak=True
        summ=0
        for i in words:


            for k in i:
                lst.append(k)
                

            for j in lst:
                if j in i:
                    count+=1
                else:
                    cheak=False
                    break
            
            if cheak:
                summ+=1
            count=0
            cheak=False

        return summ-1