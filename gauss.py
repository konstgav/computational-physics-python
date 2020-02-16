from numpy.linalg import solve
import numpy as np
A = np.array([[1,2,3],[2,5,3],[6,2,1]],float)
v = np.array([4,3,2],float)
x = solve (A,v)
print(x)

def gauss(A,v):
    N = v.size
    x = np.empty(N, float)
    
    # Gauss eliminaton
    for i in range(N):
        div = A[i,i]
        A[i,:] /= div
        v[i] /= div
        
        for j in range(i+1,N):
            mult = A[j,i]
            A[j,:] -= mult*A[i,:]
            v[j] -= mult*v[i]

    # backward substitution
    for i in range(N-1,-1,-1):
        x[i] = v[i]
        for j in range(i+1,N):
            x[i] -= A[i,j]*x[j]

    return x

print(gauss(A,v))