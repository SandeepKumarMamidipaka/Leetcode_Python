class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=[]
        for i in range(len(s)):
            c=0
            for j in range(len(s)):
                if(s[i]==s[j]):
                    c+=1
            count.append(c)
        # print(count)
        for i in range(len(count)-1):
            if(count[i]!=count[i+1]):
                return False
        return True
        
