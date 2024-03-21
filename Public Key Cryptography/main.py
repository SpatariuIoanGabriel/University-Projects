# Algorithm for determining all bases b with respect to which a composite odd number n is pseudoprime. Use the repeated squaring modular exponentiation method.
# a composite number is a positive number that is not prime
# a number is called pseudoprime to the base b if (b,n) = 1 and b^(n−1) = 1 (mod n) holds

def modular_pow(base, exponent, modulus):
    # Here we compute the result of b^(n−1) (mod n) for any b and n.
    result = 1
    while exponent > 0:
        # When the exponent become zero, we exit the while because we don t have anything to compute.
        if exponent % 2 == 1:
            # If the exponent is odd, we save in result the value
            result = (result * base) % modulus
        # The base is squared repeatedly
        base = (base * base) % modulus
        # The exponent is halved, because we square the base
        exponent //= 2
        #We do this until the exponent reaches 0
    return result


def is_pseudoprime(n, b):
    # If n is not positive or n is not odd, return false
    if n <= 1 or n % 2 == 0:
        return False

    # Calculate (b^(n-1)) % n
    result = modular_pow(b, n - 1, n)

    if result == 1:
        return True
    else:
        return False

def find_pseudoprime_bases(n):
    pseudoprime_bases = []

    # Try all possible bases from 1 to n-1
    for b in range(1, n):
        if is_pseudoprime(n, b):
            pseudoprime_bases.append(b)

    return pseudoprime_bases

n = 91
pseudoprime_bases = find_pseudoprime_bases(n)

if pseudoprime_bases:
    print(f"Pseudoprime bases for {n}: {pseudoprime_bases}")
else:
    print(f"{n} is not a pseudoprime for any base.")
