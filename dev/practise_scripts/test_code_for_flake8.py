settings = {"a": 1, "b": 2, "c": 3}


def fibonachi(s1, s2, n):
    """
    calculates the fibonachi sequence
    with given custom numbers
    """
    result = [s1, s2]
    for i in range(n):
        s1, s2 = s2, s1 + s2
        result.append(s2)
    return result


def fibonachi_standard(n):
    """
    calculates the standard fibonachi sequence
    """
    return fibonachi(s1=1, s2=2, n=n)
