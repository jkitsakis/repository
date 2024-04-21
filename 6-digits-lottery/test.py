from itertools import combinations

# Given numbers
numbers = [12, 13, 45, 37, 46, 27, 28]

# Calculate and display all 6-digit combinations
six_digit_combinations = list(combinations(numbers, 6))

# Display the combinations
for combination in six_digit_combinations:
    print(combination)
