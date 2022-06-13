# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A:list):
    # write your code in Python 3.6
    # print(f"A = {A}")
    
    # empty list
    if not A:
        return 0
    
    # one item list
    if len(A) == 1:
        return A[0]
    
    # check if it is even list. 
    if len(A) % 2 == 0:
        return 0
    
    # count how many each item is exist within the list
    itemdict = {}
    for item in A:
        cnt_item = (itemdict.get(item) + 1) if item in itemdict else 1        
        itemdict.update({item: cnt_item})
            # print (f"final itemdict = {itemdict}")

    result = 0
    for k, v in itemdict.items():
        # print(f"{k} = {v}")
        if (v % 2) != 0:
            result = k
    
    return result