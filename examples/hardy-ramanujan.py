import math
from decimal import Decimal, getcontext

def hardy_ramanujan_approx(n):
    # 1. Set Precision
    # The result is massive, so we need a lot of digit slots.
    getcontext().prec = 500 

    # Convert inputs to Decimal for high precision math
    n_dec = Decimal(n)
    pi = Decimal(3.14159265358979323846)
    sqrt_3 = Decimal(3).sqrt()
    
    # 2. The Exponent Part: pi * sqrt(2n / 3)
    exponent = pi * ( (2 * n_dec) / 3 ).sqrt()
    
    # 3. The Multiplier Part: 1 / (4n * sqrt(3))
    multiplier = 1 / (4 * n_dec * sqrt_3)
    
    # 4. Combine them: multiplier * e^(exponent)
    # .exp() calculates e to the power of the exponent
    result = multiplier * exponent.exp()
    
    return result

# --- Settings ---
my_target = 10

print(f"Calculating approximation for Target {my_target}...")

# This happens instantly
approx_value = hardy_ramanujan_approx(my_target)

# Print the result (Scientific notation first because it's huge)
print(f"Approximate Ways: {approx_value:.5e}")