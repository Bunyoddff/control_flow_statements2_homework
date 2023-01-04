def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    d1=n//10000
    d2=(n//1000)%10
    d3=(n//100)%10
    d4=((n//10)%100)%10
    d5=n%10
    s=0
    m=max(d1,d2,d3,d4,d5)
    if d5==m:
        return 1
    elif d4==m:
        return 2
    elif d3==m:
        return 3
    elif d2==m:
        return 4
    elif d1==m:
        return 5
    
print(main(76514))