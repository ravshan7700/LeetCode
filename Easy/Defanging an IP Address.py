class Solution:
    def defangIPaddr(self, address: str) -> str:
        a=address.split(".")
        address=""
        index=0
        while index<len(a):
            address+=a[index]
            if index==len(a)-1:
                pass
            else:
                address+="[.]"
            index+=1
        
        return address

sp=Solution()
print(sp.defangIPaddr("1.2.3.4"))
            
