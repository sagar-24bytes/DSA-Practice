class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if target==nums[mid]:
                return mid
            if nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right-=1
                else:
                    left+=1
            else:
                if nums[mid]<target<=nums[right]:
                    left+=1
                else:
                    right-=1
        return -1
        