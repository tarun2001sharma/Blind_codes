class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False  # Flag to track if the first row needs to be zeroed
        first_col_zero = False  # Flag to track if the first column needs to be zeroed

        # Step 1: Determine which rows and columns need to be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_zero = True  # Mark that the first row should be zeroed
                    if j == 0:
                        first_col_zero = True  # Mark that the first column should be zeroed
                    matrix[i][0] = 0  # Mark the first element of the row
                    matrix[0][j] = 0  # Mark the first element of the column

        # Step 2: Use the markers to set rows and columns to zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Zero out the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 4: Zero out the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
