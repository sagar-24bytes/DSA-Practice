class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapify(nums,n,i):
            while True:
                largest=i
                left=2*i+1
                right=2*i+2

                if left<n and nums[left]>nums[largest]:
                    largest=left
                if right<n and nums[right]>nums[largest]:
                    largest=right
                if largest==i:
                    break
                nums[i],nums[largest]=nums[largest],nums[i]
                i=largest
        n=len(nums)
        for k in range(n//2-1,-1,-1):
            heapify(nums,n,k)
        for j in range(n-1,0,-1):
            nums[0],nums[j]=nums[j],nums[0]
            heapify(nums,j,0)
        return nums
        

        