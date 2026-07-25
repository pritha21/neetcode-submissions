class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        while start<end:
            diff=target-numbers[start]
            if diff<numbers[end]:
                end=end-1
            elif diff>numbers[end]:
                start=start+1
            else:
                return [start+1,end+1]
        