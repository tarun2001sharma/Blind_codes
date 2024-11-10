class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the triangle
        triangle = []
        
        for row in range(numRows):
            # Start a new row with 1
            current_row = [1] * (row + 1)
            
            # Fill in the intermediate values
            for j in range(1, row):
                current_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
            
            # Append the current row to the triangle
            triangle.append(current_row)
        
        return triangle
