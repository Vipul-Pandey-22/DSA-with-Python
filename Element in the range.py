class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        cnt = 0
        for i in range(A, B+1):
            if i in arr:
                pass
            else:
                return False
        return True
