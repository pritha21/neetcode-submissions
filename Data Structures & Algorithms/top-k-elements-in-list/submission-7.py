class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for n in nums:
            if n in seen:
                seen[n]+=1
            else:
                seen[n]=1

        sorted_seen=sorted(seen.items(),key= lambda item:item[1], reverse=True)
        top_k=[item[0] for item in sorted_seen[:k]]
        return top_k
           
        




        