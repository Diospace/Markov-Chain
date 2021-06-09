import numpy as np
import sys
#Linear equation and markov chain solution
#this program is Write By Endurance ogun and is part of the Sfip program
#CopyRight:: can be use for any of your project but one should not delete this comment or claim ownship of the program.
#sign by the Sfip.inc
def Markov_chain(A,n):
    x=np.zeros(n)
    for i in range(n):
        if A[i,i]==0.0:
            sys.exit("Can't divide by 0")
        for j in range(i+1,n):
            ratio=A[i,j]/A[i,i]
            for k in range(n+1):
                A[j,k] = A[j,k] - (ratio * A[i,k])
    x[A.shape[0]-1]=A[A.shape[0]-1,A.shape[0]]/A[A.shape[0]-1,A.shape[0]-1]
    for i in range(n-2,-1,-1):
        x[i]=A[i,A.shape[0]]
        for j in range(i + 1, A.shape[0]):
            x[i] = x[i] - A[i,j] * x[j]
        x[i] = x[i] / A[i,i]

    print('\nThe solution is: ')
    for i in range(A.shape[0]):
        print('X%d = %0.2f' % (i, x[i]), end='\t')

def get_matrixA(m_len,variable_type=float):
    k=0
    A=[]
    B=[]
    M=[]
    n=m_len+1
    for i in range(1,n+1):
        for j in range(1,n):
            if i == n:
                k+=1
                m_col_row = float(input("enter value for \n b" + str(k) + "::"))
                A.append(m_col_row)
                B.append(m_col_row)

            else:
                m_col_row= float(input("enter value for \n a"+str(i)+str(j)+"::"))
                A.append(m_col_row)
                M.append(m_col_row)

    B = np.array(B).reshape(n-1, 1)
    D = np.array(M).reshape(n-1, n-1)
    print(D)
    print(B)

    A=np.array(A).reshape(n-1,n)
    return A




def get_solution():
    N=int(input("NxN dimension of Matrix::"))
    A=get_matrixA(N)

    Markov_chain(A,N)


get_solution()