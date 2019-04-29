from random import randint as rint
import math
# RSA key fun stuff
# Reference: https://www.di-mgt.com.au/rsa_factorize_n.html


# Try to find factor of n given a random g
def factor_n(k, g, n):
    t = k
    if t % 2 == 0:
        t = t / 2
        x = (g**t) % n
        y = math.gcd(x-1, n)
        if x > 1 and y > 1:
            p = y
            q = n / y
            return (p, q)
        else:
            factor_n(t, g, n)
    else:
        return -1
    return 1


# Main driver
def main():
    n = 1259531756783983515701499777642110356794201569384295868500005799617750548880147110509521944049285041602433244172023804646590835427723055191592144638318476432867385429617360121
    e = 65537
    d = 879829162542850074748838973716462641470292321076843078870413133138541894315167534655428516005898396122103324293925057981802023330186106794090644952807381680714475934931163153

    k = (d * e) - 1
    g = rint(1, n)
    rounds = 0
    print("Attempting using g = {}".format(g))
    solution = factor_n(k, g, n)
    rounds += 1
    while solution == -1:
        g = rint(1, n)
        print("Attempting using g = {}".format(g))
        solution = factor_n(k, g, n)
        rounds += 1
    print("P = {}, Q = {}".format(solution[0], solution[1]))
    print("Solution took {} random samplings of 'g' to terminate".format(rounds))


if __name__ == '__main__':
    main()
