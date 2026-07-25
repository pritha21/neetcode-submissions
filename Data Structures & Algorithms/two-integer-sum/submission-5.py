class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set={}
        for i in range(len(nums)):
            num_set[nums[i]]=i
           
        
        for j in range(len(nums)):
            diff=target-nums[j]
    
            if diff in num_set and num_set[diff]!=j:
                if num_set[diff]<j:
                    return[num_set[diff],j]
                else:
                    return[j,num_set[diff]]
            



        