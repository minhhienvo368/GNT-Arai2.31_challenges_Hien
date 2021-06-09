# Given a binary input string,
# your program should produce a decimal output.
# The program should handle invalid inputs.

# First: check if digits is not a binary string, return True
# COACHES' NOTE: use snake case for names, not camel case.
def notBinary(digits: str) -> bool:
    # COACHES' NOTE: too compact and hard to read, spread out your code across your function in properly named variables.
    return any(digit not in ['0', '1'] for digit in digits)


def parse_binary(digits: str) -> int:
    # get a binary string, return a decimal, interger value
    # exception if invalid string
    if notBinary(digits):
        raise ValueError("Not all binary digits in '", digits, "'")
    # COACHES' NOTE: else statement is not needed since raising an error returns out of the function.
    else:                       # OK - calculate sum of powers of 2
        # COACHES' NOTE: what is going on here? very hard to read, spread this out across your function.
        return sum(pow(2, (len(digits) - 1 - i))
                   for i, digit in enumerate(digits)
                   if (digit == '1'))

        # example: 101 => 1*2^2 + 0*2^1 + 1*2^0 => 1*4 + 0*2 + 1*1 => 4 + 1 => 5

# COACHES' NOTE: clean up.
# parse_binary('10')
parse_binary("11010")

# COACHES' NOTE: You sacrificed readability for compactness and tried to explain the code in the comments. Code should explain itself, use proper naming. Rather too many variables than too little.
