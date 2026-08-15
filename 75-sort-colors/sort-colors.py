class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0,c1,c2=0,0,0
        for n in nums:
            if n==0:
                c0+=1
            elif n==1:
                c1+=1
            else:
                c2+=1
        i=0
        while i<c0:
            nums[i]=0
            i+=1
        j=0
        while j<c1:
            nums[i]=1
            j+=1
            i+=1
        k=0
        while k<c2:
            nums[i]=2
            k+=1
            i+=1
        
        
            
        