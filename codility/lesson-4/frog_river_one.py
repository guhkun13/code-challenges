def solution(X, A):
    # print(f'x = {X} | A = {A}')

    # array kosong = tidak ada daun jatuh
    N = len(A)
    if N < 1:
        return -1

    # misalkan mau ke titik 7, berarti harus ada 7 posisi daun yg lengkap
    # 1 s.d 7
    leafs = set()    
    is_complete = False
    is_equal = lambda x,y: True if x == y else False

    idx = 0
    while idx < N and not is_complete:        
        leafs.add(A[idx])
        idx += 1
        is_complete = is_equal(len(leafs), X)
        
    if is_complete:        
        idx -= 1
        return idx
    
    return -1

