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
    if a<b<c or c<b<a or a>b>c or c>b>a:
        return b
    elif b<a<c or c<a<b or b>a>c or c>a>b:
        return a
    elif a<c<b or b<c<a or a>c>b or b>c>a:
        return c
    elif a==b!=c:
        return b
    elif a==c!=b:
        return c
     
print(main(5,5,-1))
