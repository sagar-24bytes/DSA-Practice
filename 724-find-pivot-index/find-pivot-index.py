class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        curr_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            left_sum=curr_sum-nums[i]
            right_sum=total-curr_sum
            if left_sum==right_sum:
                return i
        return -1

        