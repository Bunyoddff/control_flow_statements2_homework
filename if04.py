def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    s=max(a,b)
    if a==b:
        return 0
    else:
        return s
print(main(5,5))