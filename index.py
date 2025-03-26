def reverse_number(n):
    rev = 0  # Initialize the reversed number as 0
    while n > 0:  # Loop until the number becomes 0
        rev = rev * 10 + (n % 10)  # Extract the last digit and append it to rev
        n //= 10  # Remove the last digit from n
    return rev  # Return the reversed number
 
def sum_of_digits(n):
    total = 0  # Initialize sum as 0
    while n > 0:  # Loop until n becomes 0
        total += n % 10  # Extract last digit and add to total
        n //= 10  # Remove the last digit
    return total  # Return the sum

def count_digits(n):
    count = 0  # Initialize count as 0
    while n > 0:  # Loop until n becomes 0
        count += 1  # Increment count
        n //= 10  # Remove last digit
    return count  # Return total count of digits

def print_multiples_of_3(n):
    while n > 0:  # Loop until n becomes 0
        digit = n % 10  # Extract last digit
        if digit % 3 == 0:  # Check if digit is a multiple of 3
            print(digit, end=" ")  # Print the digit
        n //= 10  # Remove last digit

# Given number
num1 = 54312

# Reverse number
rev_num = reverse_number(num1)
print("Reversed Number:", rev_num)  # Output: 21345

# Sum of digits
sum_digits = sum_of_digits(num1)
print("Sum of Digits:", sum_digits)  # Output: 15

# Count of digits
digit_count = count_digits(num1)
print("Number of Digits:", digit_count + 1)  # Output: 6 (5 + 1)

# Print multiples of 3
print("Multiples of 3 in the number:", end=" ")
print_multiples_of_3(num1)  # Output: 3
