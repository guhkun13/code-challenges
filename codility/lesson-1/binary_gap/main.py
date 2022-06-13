# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def decimalToBinary(n):  
    return bin(n).replace("0b", "") 

def solution(N):
    # write your code in Python 3.6
    print(f"N= {N}")
    bn = decimalToBinary(N)
    print(f"bn= {bn}")

    if not '0' in bn:
        print('zero not exist. return')
        return 0

    sbn = bn.split('1')
    print(f"sbn= {sbn}")        

    if len(sbn) < 3:
        return 0
      
    # check the end of list, is it empty ? empty == 1
    endsbn = sbn[-1]
    print(f"endsbn = {endsbn}")
    
    if endsbn != "":
      print("bukan 1")
      sbn = sbn[:len(sbn)-1]
      print(f"update sbn= {sbn}")
        
    print(f"-- new sbn= {sbn}")
    # iterate each item, 
    # count item length and check if there are any char beside 0
    maxlen = 0
    for x in sbn:
        print(f"x = {x}")
        valid_str = '0' * len(x)
        if valid_str == x and len(x) > maxlen:
            maxlen = len(x)
    
    print(f"maxlen = {maxlen}")
    return maxlen
    
t1 = solution(20)
t2 = solution(328)
t3 = solution(6)

print(f"t1 = {t1}")
print(f"t2 = {t2}")
print(f"t3 = {t3}")