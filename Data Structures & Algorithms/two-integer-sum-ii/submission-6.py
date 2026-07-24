class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set=set(numbers)
        for num in num_set:
            diff=target-num
            if diff in num_set and num!=diff:
                index1=numbers.index(num)+1
                index2=numbers.index(diff)+1
                if index1<index2:
                    return[index1,index2]
                else:
                    return[index2,index1]
                
            
        return -1
        