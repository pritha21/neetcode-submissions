class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set={}
        for i in range(len(nums)):
            num_set[nums[i]]=i
        for j in range(len(nums)):
            diff=target-nums[j]
            if diff in num_set and num_set[diff]!=j:
                return [j,num_set[diff]]
            

        
        
        
        
        
        
        
        
        #for i in range(len(nums)-1):
            #for j in range(i+1, len(nums)):
                #if nums[i]+nums[j]==target:
                    #return [i,j]
                


  



        