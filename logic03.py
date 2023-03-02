def main(a=7,b=7):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    a = 9
    b = 7
    answer = (a == b)
    return answer

print(main())