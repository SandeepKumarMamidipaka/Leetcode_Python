class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        list1=[]
        for i in range(len(arr)):
            c=0
            for j in range(len(arr)):
                if arr[i]==arr[j]:
                    c+=1
            if c==1:
                list1.append(arr[i])
        if(k<=len(list1)):
            return list1[k-1]
        return ""
        
