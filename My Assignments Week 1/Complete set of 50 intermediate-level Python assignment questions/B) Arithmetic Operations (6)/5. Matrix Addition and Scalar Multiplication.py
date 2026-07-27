# 5. Matrix Addition and Scalar Multiplication
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j]+=B[i][j]
print(f'Addition: {A}')
# multiplication
B = [[5,6],[7,8]]
k = 3
for r in range(len(B)):
    for c in range(len(B[0])):
        B[r][c]*= k 
print(f'Scalar Multiplication: {B}')