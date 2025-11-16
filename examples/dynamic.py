def count_unrestricted_partitions(target):
    # 1. Dynamic Coins: Use all numbers from 1 up to the target
    # If target is 12, coins will be [1, 2, 3, ..., 12]
    coins = list(range(1, target + 1))
    
    # 2. Create the table
    ways_table = [0] * (target + 1)
    
    # Base Case: 1 way to make 0
    ways_table[0] = 1

    # 3. The Loop
    for coin in coins:
        for current_amount in range(coin, target + 1):
            ways_table[current_amount] = ways_table[current_amount] + ways_table[current_amount - coin]

    return ways_table

# --- Settings ---
my_target = 10

# Get the table
full_table = count_unrestricted_partitions(my_target)

# Print results for 0, 1, 2 ... up to my_target
print(f"Calculating partitions for 0 to {my_target}")
print("-" * 30)

for number in range(0, my_target + 1):
    print(f"Target {number}: {full_table[number]} ways")

# Add Total at the end
print("-" * 30)
print(f"TOTAL ways to partition {my_target}: {full_table[my_target]}")