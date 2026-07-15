class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        for num in nums:
            res[num]=res.get(num,0)+1
        sorted_nums=sorted(res.keys(),key=res.get,reverse=True)
        return sorted_nums[:k]