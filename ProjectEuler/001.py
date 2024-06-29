# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

from functools import reduce


def is_multiple_of_3_or_5(num):
    return num % 3 == 0 or num % 5 == 0


LIMIT = 1000

total_sum = reduce(
    lambda accumulator, val: accumulator + val,
    filter(is_multiple_of_3_or_5, range(LIMIT)),
)

print("Sum of multiples of 3 or 5 below 1000:", total_sum)
