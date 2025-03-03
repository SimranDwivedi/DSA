class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        first=[]
        pivotar=[]
        last=[]
        for i in nums:
            if i<pivot:
                first.append(i)
            elif i==pivot:
                pivotar.append(i)
            else:
                last.append(i)
        first.extend(pivotar)
        first.extend(last)
        return first