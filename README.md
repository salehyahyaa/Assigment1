# Assignment 1 – Fermat's Last Theorem Near Miss Search

## Description

This program searches for **near misses** of Fermat's Last Theorem.

Fermat's Last Theorem states that there are no positive integers `x`, `y`, `z` and `n > 2` such that:

```
x^n + y^n = z^n
```

This program looks for combinations where `x^n + y^n` is *close* (but not equal) to some perfect `n`-th power `z^n`, and reports the pair with the **smallest relative miss**.

## File

| File | Description |
|------|-------------|
| `assignment1_near_miss_fermat.py` | Main Python script |

## Usage

Run the script with Python 3:

```bash
python assignment1_near_miss_fermat.py
```

You will be prompted for:

- **n** – the exponent power (must satisfy `2 < n < 12`)
- **k** – the upper bound for `x` and `y` (must be `>= 10`)

The program then searches all pairs `(x, y)` with `10 ≤ x ≤ k` and `10 ≤ y ≤ k`, computing:

```
miss         = min(|x^n + y^n - z^n|, |(z+1)^n - x^n - y^n|)
relative miss = miss / (x^n + y^n)
```

Whenever a new smallest relative miss is found it is printed immediately.  
After all pairs are checked, the best near miss found overall is printed.

## Example Output

```
Enter n (power), must satisfy 2 < n < 12: 3
Enter k (upper bound for x and y), must be >= 10: 20

New best near miss found:
x = 10
y = 10
z = 12
miss = 64
relative miss = 3.200000000000e-03

...

BEST (smallest) near miss found overall:
x = ...
y = ...
z = ...
miss = ...
relative miss = ...
```

## Requirements

- Python 3.6 or later (uses f-strings)
- No external libraries required