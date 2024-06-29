# The prime factors of 13195 are 5, 7, 13, and 29.
#
# What is the largest prime factor of the number 600851475143?


def largest_prime_factor(n):
    while n % 2 == 0:
        largest_prime = 2
        n //= 2

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_prime = factor
            n //= factor
        factor += 2

    if n > 2:
        largest_prime = n

    return largest_prime


TEST_CASE = 600851475143
print("Largest prime factor:", largest_prime_factor(TEST_CASE))
