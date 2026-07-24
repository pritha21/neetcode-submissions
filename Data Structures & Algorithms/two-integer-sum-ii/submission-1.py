class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        check = 0
        for i in range(len(numbers)):
            check = numbers[i]
            for j in range(1, len(numbers)):
                if check + numbers[j]==target:
                    return [i+1,j+1]
                
        return -1
        