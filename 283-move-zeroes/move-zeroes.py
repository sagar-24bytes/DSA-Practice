class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        update=0
        for n in range(len(nums)):
            if nums[n]!=0:
                nums[update]=nums[n]
                update+=1
        while update<len(nums):
            nums[update]=0
            update+=1
        