class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sets=sorted(set(nums))
        longest=current=1
        for i in range(1,len(sets)):
            if sets[i-1]+1==sets[i]:
                current+=1
            else:
                longest=max(longest,current)
                current=1
        return max(longest,current)