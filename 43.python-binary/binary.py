# Given a binary input string,
# your program should produce a decimal output.
# The program should handle invalid inputs.

# First: check if digits is not a binary string, return True
def notBinary(digits: str) -> bool:
    return any(digit not in ['0', '1'] for digit in digits)


def parse_binary(digits: str) -> int:
    # get a binary string, return a decimal, interger value
    # exception if invalid string
    if notBinary(digits):
        raise ValueError("Not all binary digits in '", digits, "'")
    else:                       # OK - calculate sum of powers of 2
        return sum(pow(2, (len(digits) - 1 - i))
                   for i, digit in enumerate(digits)
                   if (digit == '1'))

        # example: 101 => 1*2^2 + 0*2^1 + 1*2^0 => 1*4 + 0*2 + 1*1 => 4 + 1 => 5


# parse_binary('10')
parse_binary("11010")