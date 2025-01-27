import numpy as np

# --- Getting input from user
n = int(input("Enter the dimension of matrix"))

# --- Declaring and initializing matrix
arr = np.zeros((n,n))

# --- Getting input for elements
print("Enter elements of the matrix: ")
for i in range (n):
    for j in range (n):
        arr[i][j] = int(input(f"Enter element {i}, {j}: "))
        
sum = 0

for i in range (n):
    sum = sum+arr[i][i]
    
print(f"The sum of the diagonal of the matrix: {sum:.0f}")

