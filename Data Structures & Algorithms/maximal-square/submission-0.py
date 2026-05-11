class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0 # side length of the final square
        i = 0

        ###############################################
        # Base Case
        # ---------
        # 
        # ans = 1 if matrix[i][j] = 1 for all i and j
        ###############################################
        while i<m:
            j = 0
            while j<n:
                ans = max(ans, int(matrix[i][j]))
                j += 1
            i += 1

        table = [[0] * n for _ in range(m)]

        ###############################################
        # Table Boundary Initialization
        ###############################################
        i, j = 0, 0
        while j<n:
            table[0][j] = int(matrix[0][j])
            j += 1
        while i<m:
            table[i][0] = int(matrix[i][0])
            i += 1
        
        ###############################################
        # Induction: Table Look-up
        ###############################################
        i = 1
        while i<m:
            j = 1
            while j<n:
                if matrix[i][j]=='1':
                    tmp = (table[i][j-1], table[i-1][j], table[i-1][j-1])
                    table[i][j] = min(tmp) + 1
                    ans = max(ans, table[i][j])
                j += 1
            i += 1
        return ans*ans