def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """

    a = 15
    b = 25
    c = 35

    answer = 15 <= 25 < 35
    return answer

print(main(15,25,35))


