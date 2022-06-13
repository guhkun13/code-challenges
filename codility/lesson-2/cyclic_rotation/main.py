def solution(A:list, K:int):
    # write your code in Python 3.6
    # print(f"A  = {A} | K = {K}")    
    if not A:
        return A

    while K > 0:
        last_item = A[-1]        
        A.insert(0, last_item)
        A.pop(-1)

        # print(f"A = {A}")
        K -= 1
    return A