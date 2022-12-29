def main(n):
    """
    Find the largest digit of the five-digit number.
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
    s=max(d1,d2,d3,d4,d5)
    return s
print(main(23546))