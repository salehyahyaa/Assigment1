"""
Fermat's Last Theorem Near Miss Search| Searches for near misses of Fermat’s Last Theorem:
    x^n + y^n ≠ z^n
for:
    2 < n < 12
    10 ≤ x ≤ k
    10 ≤ y ≤ k
and z chosen so that z^n <= x^n + y^n < (z+1)^n.

Whenever a new smallest relative miss is found, prints i, At the end, prints the best near miss found overall.
"""
import math


def get_valid_int(prompt, is_valid, error_message):
    # Re-prompts until user enters a valid integer that passes is_valid(value).
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Invalid input: please enter an integer.")
            continue

        if not is_valid(value):
            print(error_message)
            continue

        return value


def integer_nth_root_floor(a, n):
    # Returns floor(a^(1/n)) using integer-only binary search.
    if a < 0:
        raise ValueError("a must be non-negative.")
    if n <= 0:
        raise ValueError("n must be positive.")
    if a in (0, 1):
        return a

    # Find an upper bound hi where hi^n > a by doubling.
    lo = 0
    hi = 1
    while pow(hi, n) <= a:
        hi *= 2

    # Binary search for the largest lo such that lo^n <= a.
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if pow(mid, n) <= a:
            lo = mid
        else:
            hi = mid

    return lo


def print_report(title, x, y, z, miss, rel):
    print()
    print(title)
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")
    print(f"miss = {miss}")
    print(f"relative miss = {rel:.12e}")


def main():
    # Read n and k with the required constraints.
    n = get_valid_int(
        "Enter n (power), must satisfy 2 < n < 12: ",
        lambda v: 2 < v < 12,
        "n must be an integer with 2 < n < 12."
    )

    k = get_valid_int(
        "Enter k (upper bound for x and y), must be >= 10: ",
        lambda v: v >= 10,
        "k must be an integer >= 10."
    )

    # Track the best (smallest) relative miss seen so far.
    best_rel = None
    best_x = best_y = best_z = best_miss = None

    # Loop over all x values from 10..k (inclusive).
    for x in range(10, k + 1):
        x_pow = pow(x, n)  # Precompute x^n once per x.

        # Loop over all y values from 10..k (inclusive).
        for y in range(10, k + 1):
            y_pow = pow(y, n)
            sum_val = x_pow + y_pow  # sum_val = x^n + y^n

            # Efficiently estimate z as floor(sum_val^(1/n)) without looping over z.
            z = integer_nth_root_floor(sum_val, n)

            # Compute misses from z^n and (z+1)^n and take the smaller one.
            z_pow = pow(z, n)
            zp1_pow = pow(z + 1, n)
            miss1 = sum_val - z_pow
            miss2 = zp1_pow - sum_val
            miss = miss1 if miss1 <= miss2 else miss2

            # Relative miss = miss / sum_val
            rel = miss / sum_val

            # If we found a new best relative miss, record it and print it immediately.
            if best_rel is None or rel < best_rel:
                best_rel = rel
                best_x, best_y, best_z, best_miss = x, y, z, miss
                print_report("New best near miss found:", best_x, best_y, best_z, best_miss, best_rel)

    # Final summary
    print_report("BEST (smallest) near miss found overall:", best_x, best_y, best_z, best_miss, best_rel)


if __name__ == "__main__":
    main()
