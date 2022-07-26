class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_so_far = -2147483647 - 1
        max_ending_here = 0
        
        for i in range(0, len(arr)):
            max_ending_here = max_ending_here + arr[i]
            
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                
            if max_ending_here < 0:
                max_ending_here = 0
                
        return max_so_far
