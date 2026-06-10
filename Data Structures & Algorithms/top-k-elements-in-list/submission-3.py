class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freq={} 

       for num in nums: 
        freq[num] = freq.get(num, 0)+1 
        # create the bucket where 
        buckets = [[] for _ in range(len(nums) +1)]
        # place numbers into their freq bucket   
        for num, count in freq.items(): 
            buckets[count].append(num) 
        
       # gather the top k frequent elements from high to low frequency
       result=[] 
       for i in range(len(buckets)-1, 0, -1): 
        for num in buckets[i]:
            result.append(num) 
            if len(result) == k: 
                return result 

            
    
        