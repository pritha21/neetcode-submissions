class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set={}
        for i in range(len(numbers)):
            num_set[numbers[i]]=i
           
        
        for j in range(len(numbers)):
            diff=target-numbers[j]
    
            if diff in num_set and num_set[diff]!=j:
                if num_set[diff]<j:
                    return[num_set[diff]+1,j+1]
                else:
                    return[j+1,num_set[diff]+1]
        