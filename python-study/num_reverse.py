def reverse_number_while(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Add to reversed number
        num //= 10  # Remove the last digit
    return reversed_num

number = 12345
reversed_result = reverse_number_while(number)
print(f"Original: {number}, Reversed: {reversed_result}")