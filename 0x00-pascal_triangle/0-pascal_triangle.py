#!/usr/bin/python3
'''Pascal Triangle'''

def pascal_triangle(n):
  """
  Generate Pascal's Triangle up to the n-th row.
  Args: n (int): The number of rows in Pascal's Triangle to generate.
  Returns: A list containing lists, where each inner list represents a row in Pascal's Triangle.
  """
  if n <= 0:
    return []
    
  """Initialize Pascal's Triangle with the first row"""
  triangle = [[1]]

for i in range(1, n):
  past_row = traingle[i - 1] """Get the last row"""
  new_row = triangle[1] """Start each row with 1"""
  
"""Generate the middle values of the row"""
for j in range(1, i):
  new_row.append(past_row[j - 1] + past_row[j])

new_row.append(1) """End each row with 1"""
triangle.append(new_row) """Add the new row to the triangle"""

return triangle
