def isDominant(A):
    size = len(A)
    for i in range(size):
        diagonal = abs(A[i][i])
        rowSum = sum([abs(number) for number in A[i]]) - diagonal
        if rowSum > diagonal:
            return False
    return True

def jacobi(A,x,b):
    size = len(A)
    iteration = 0
    epsilon = 0.001
    while True:
        oldX = x.copy()
        print('iteration ', iteration, ': ', x)
        for i in range(size):
            sumX = 0
            for j in range(size):
                if i != j:
                    sumX += A[i][j]*oldX[j]
            x[i] = (b[i] - sumX)/A[i][i]
        condition = abs(x[0] - oldX[0])
        if condition < epsilon:
            break
        iteration += 1
    print('iteration ', iteration + 1, ': ', x)

def gaussSeidel(A,x,b):
    size = len(A)
    iteration = 0
    epsilon = 0.001
    while True:
        oldX = x.copy()
        print('iteration ', iteration, ': ', x)
        for i in range(size):
            sumX = 0
            for j in range(size):
                if i != j:
                    sumX += A[i][j]*x[j]
            x[i] = (b[i] - sumX)/A[i][i]
        condition = abs(x[0]-oldX[0])
        if condition < epsilon:
            break
        iteration += 1
    print('iteration ', iteration + 1, ': ', x)

A = [[4, 2, 0],
     [2, 10, 4],
     [0, 4, 5]]
x = [0, 0, 0]
b = [2, 6, 5]

print('Jacobi method:')
jacobi(A,x,b)

A = [[4, 2, 0],
     [2, 10, 4],
     [0, 4, 5]]
x = [0, 0, 0]
b = [2, 6, 5]

print('\ngauss-Seidel method:')
gaussSeidel(A,x,b)