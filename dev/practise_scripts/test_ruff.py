from numpy import *

def fibonachi(s1, s2, n):
    result = [s1, s2]
    for i in range(n):
        s1, s2 = s2, s1 + s2
        result.append(s2)
    return result

if __name__ == "__main__":
    print(fibonachi(1,1,10))
