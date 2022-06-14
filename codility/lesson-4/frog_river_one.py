def solution(X, A):
    # print(f'x = {X} | A = {A}')
    # tujuannya adalah sampai ke X

    # array kosong = tidak ada daun jatuh
    N = len(A)
    if N < 1:
        return -1
    
    # misalkan mau ke titik 7, berarti harus ada 7 posisi daun yg lengkap
    # 1 s.d 7

    leaf_pos = set()
    cnt_leaf = len(leaf_pos)
    is_complete = False
    leaf_needed = X 
    idx = 0
    while idx < N and not is_complete:        
        # print(f'idx = {idx} | = {A[idx]}')
        leaf_pos.add(A[idx])
        idx += 1

        # print(f'leaf_pos = {leaf_pos}')
        cnt_leaf = len(leaf_pos)
        # print(f'cnt_leaf = {cnt_leaf} | leaf_needed = {leaf_needed}')
        is_complete = True if cnt_leaf == leaf_needed else False
        # print(f'is_complete = {is_complete}')        
        
    if is_complete:        
        idx -= 1
        # print(f'idx = {idx}')
        return idx
    
    return -1