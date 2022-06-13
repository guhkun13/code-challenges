''' Count minimal number of jumps from position X to Y. '''

import math
def solution(X, Y, D):
    N = math.ceil((Y - X) / D)

    return N