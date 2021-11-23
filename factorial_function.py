# Code

def factorial(n, list={}):
    """
    Calculate n!

    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """

    # TODO: Write your recursive factorial function here

    if n <= 1:
        return 1
    return n * factorial(n-1)


def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    # TODO: Write your recursive string reverser solution here
    if len(input) == 0:
        return ''
    else:
        first_char = input[0]
        rest = input[1:None]
        sub_input = reverse_string(rest)
        return sub_input + first_char


# Test Cases

print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")

# Test Cases

print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (120 == factorial(5)) else "Fail")