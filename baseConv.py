# Change conversionAlphabet to contain the conversion alphabet for the base you 
# are converting to, starting at the equivalent 0
# The following algorithm was adapted from here:https://codereview.stackexchange.com/questions/182733/base-26-letters-and-base-10-using-recursion
# with the alphabet starting at 0

A_UPPERCASE = ord('A')
ALPHABET_SIZE = 26

def _decompose(number):
    """Generate digits from `number` in base alphabet, least significants
    bits first.
    """

    while number:
        number, remainder = divmod(number, ALPHABET_SIZE)
        yield remainder


def base_10_to_alphabet(number):
    """Convert a decimal number to its base alphabet representation"""

    return ''.join(
            chr(A_UPPERCASE + part)
            for part in _decompose(number)
    )[::-1]


def base_alphabet_to_10(letters):
    """Convert an alphabet number to its decimal representation"""

    return sum(
            (ord(letter) - A_UPPERCASE + 1) * ALPHABET_SIZE**i
            for i, letter in enumerate(reversed(letters.upper()))
    )

# Question 1 part a)
print(base_10_to_alphabet(113229605))
# Question 1 part b)
mult = base_10_to_alphabet(base_alphabet_to_10("DALLAS") * 113229605)
print(mult)
# Question 1 part c)
quotient = base_alphabet_to_10(mult) // base_alphabet_to_10("OKC")
remainder = base_alphabet_to_10(mult) % base_alphabet_to_10("OKC")
print(base_10_to_alphabet(quotient))
print(base_10_to_alphabet(remainder))