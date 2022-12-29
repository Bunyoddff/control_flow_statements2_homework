def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and b>c:
        return b
        if b>a and a>c:
            return a
    elif a==b:
        return a
        if b==c:
            return c

    else:
        return c    
    
print(main(5,5,-1))