def solution(A):
    # base case
    if len(A) < 1:
        return 0

    P = 1
    N = len(A)
    sumA = sum(A)
    sum_left = 0
    result = []
    for i in range(N - 1):        

        # initial answer
        # sum_left = sum(A[:P])
        # sum_right = sum(A[P:])

        # improve 1
        # rumus : A + B = C, jadi B = C - A
        # sum_left = sum(A[:P])
        # sum_right = sumA - sum_left

        # improve 2
        # perhatikan bahwa, index berjalan tetap. jadi sebenarnya hanya perlu 
        # menambah item pada index yg sedang diakses ke penjumlahan sblmnya. 

        sum_left += A[P-1]
        sum_right = sumA - sum_left

        diff = abs(sum_left - sum_right)
        result.append(diff)
        P+=1
    
    return min(result)