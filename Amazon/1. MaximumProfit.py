# User function Template for python3

class Solution:
    def maxProfit(self, K, N, A):
        # code here
        dp = [[0]*(N) for i in range(K+1)]
        
        for i in range(1, K+1):
            mx = float('-inf')
            for j in range(1, N):
                mx = max(mx, dp[i-1][j-1] - A[j-1])
                print(i, j)
                dp[i][j] = max(dp[i][j-1], mx+A[j])

        return dp[K][N-1]

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])

        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends
