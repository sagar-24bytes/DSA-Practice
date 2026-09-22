from collections import Counter
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq=Counter(nums)
        i=0
        for _ in range(freq[0]):
            nums[i]=0
            i+=1
        for _ in range(freq[1]):
            nums[i]=1
            i+=1
        for _ in range(freq[2]):
            nums[i]=2
            i+=1
        


        