def take_n():
 
    A = []
    n = int(input("Enter the N for N x N matrix: "))
    return A,n
 
def t_i(n,A):
	print("Enter the elements of the matrix: ")
	for i in range(n):
		A.append([])
		for _ in range(n):
			A[i].append(int(input()))
	return A,n
 
def d_m(A):
	print("The matrix is: ")
	print(A)
 
	print("Display Array In Matrix Format: ")
def print_m(n,A):
    for i in range(n):
    	for j in range(n):
    		print(A[i][j], end=" ")
    	print()
 
A,n = take_n()
 
 
A,n = t_i(n,A)
 
d_m(A)
 
 
B,n = take_n()
 
 
B,n = t_i(n,B)
 
d_m(B)
 
result = []
 
for i in range(len(A)):
    result.append([])
    for j in range(len(B[0])):
        result[i].append(0)
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
 
print("The result of the multiplication is: ")
 
for r in result:
    print(r)
