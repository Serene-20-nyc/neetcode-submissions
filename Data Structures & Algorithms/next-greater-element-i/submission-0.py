class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ans={}
        for num in nums2:
            while (stack and stack[-1]<num):
                t=stack.pop()
                ans[t]=num
            stack.append(num)
        return [ans.get(num,-1) for num in nums1]
        