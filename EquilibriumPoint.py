# A is given Array
# N is number of element present in array

def equilibriumPoint(self,A, N):
  if len(A) == 1:
    return 1
  
  total = 0
  lst = []
  Sum = A[0]
  lst.append(Sum)
  
  # Find Prefix of array
  for i in range(1, N):
    Sum += A[i]
    lst.append(Sum)
  
  total = A[-1] # Assign Last Element to total
  for i in range(1, N):
    leftSum = lst[i] - A[i]  # Calculate leftSum 
    rightSum = total - lst[i] # Calculate rightSum
    if leftSum == rightSum:
      return (i+1)
  return -1
