def solution(A):
    
    N = len(A)
    if N < 1:
        return 0
    
    ttl_sum = (N * (N+1)) // 2
    is_sum_true =  True if sum(A) == ttl_sum else False    
    is_unique = True if N == len(set(A)) else False

    return 1 if is_sum_true and is_unique else 0


# salah satu case yang gagal : total sum nya sama, tapi angka nya gak unique, bukan permutasi. 
# N = len(A)
# jadi ada 2 kondisi yg bisa dicek. Jumlah sum nya sesuai dengan Permutasi nya, SUM(N) = (N * (N+1)) // 2 dan len(set(A)) == N
A = [1, 4, 1]
print(solution(A))

# Detected time complexity:
# O(N) or O(N * log(N))