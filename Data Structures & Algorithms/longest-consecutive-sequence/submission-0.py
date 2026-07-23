class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        start=0
        length=0
        num_set=set(nums)
        print(num_set)
        for i in num_set:
            if i-1 not in num_set:
                start=i
                length=1
                while start+1 in num_set:
                    start+=1
                    length+=1
                longest=max(longest,length)
                    

        return longest

        