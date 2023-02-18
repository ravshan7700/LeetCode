class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for_i=[]
        image2=[]
        for i in image:
            i=i[::-1]
            for j in i:
                if j==0:
                    for_i.append(1)
                else:
                    for_i.append(0)
            print(for_i)
            image2.extend(for_i)
            for_i.clear()
        return image2

asdf=Solution()
print(asdf.flipAndInvertImage([[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 1, 0]]))
    


