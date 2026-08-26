class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums)>1:
                l_arr=nums[:len(nums)//2]
                r_arr=nums[len(nums)//2:]
                merge_sort(l_arr)
                merge_sort(r_arr)
                l=r=0 # for comapring lefta nd right subarrays
                k=0 # for storing after comparsion
                while l<len(l_arr) and r<len(r_arr):
                    if l_arr[l]<r_arr[r]:
                        nums[k]=l_arr[l]
                        l+=1
                    else:
                        nums[k]=r_arr[r]
                        r+=1
                    k+=1
                while l<len(l_arr):
                    nums[k]=l_arr[l]
                    l+=1
                    k+=1
                while r<len(r_arr):
                    nums[k]=r_arr[r]
                    r+=1
                    k+=1
        merge_sort(nums)
        return nums
        