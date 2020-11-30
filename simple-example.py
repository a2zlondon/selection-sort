A = [222,34,45,45,78,67,1,43,54,656]
print(A)
for current in range(0, len(A)):
    #print(current)
    minIndex = current
    for i in range(current + 1, len(A)):
        print(A[i], A[minIndex])
        if A[i] < A[minIndex]:
            minIndex = i
    temp = A[current]
    A[current] = A[minIndex]
    A[minIndex] = temp
    print(A)
    print()
