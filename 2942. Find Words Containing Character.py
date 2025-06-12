class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        list1=[]
        i=0
        for s in words:
            if x in s:
                list1.append(i)
            i+=1
        return list1
