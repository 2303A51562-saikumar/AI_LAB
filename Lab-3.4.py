# Task 1:-Zero-shot Prompt – Fibonacci Series Generator
# Function to print the first n Fibonacci numbers
def print_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

print_fibonacci(7)


# Task 2:-One-shot Prompt – List Reversal Function.
# Function to reverse a list
# Example: reverse_list([1, 2, 3]) returns [3, 2, 1]
def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1, 2, 3]))



# Task 3:-Few-shot Prompt – String Pattern Matching
# Function to check if a string starts with a capital letter and ends with a period
# Example: is_valid("Hello.") returns True
# Example: is_valid("hello.") returns False
# Example: is_valid("Hello") returns False
def is_valid(s):
    return len(s) > 0 and s[0].isupper() and s[-1] == '.'

print(is_valid("Hello."))
print(is_valid("hello."))
print(is_valid("Hello"))



# Task 4:-Zero-shot vs Few-shot – Email Validator
# Function to validate an email address
def is_valid_email(email):
    return '@' in email and '.' in email.split('@')[-1]

print(is_valid_email("example@example.com"))
print(is_valid_email("invalid-email"))


# Function to validate an email address with examples
def is_valid_email_few_shot(email):
    if '@' not in email or email.count('@') != 1:
        return False
    username, domain = email.split('@')
    if len(username) == 0 or len(domain) == 0:
        return False
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return False
    return True

print(is_valid_email_few_shot("example@example.com"))  # True
print(is_valid_email_few_shot("invalid-email"))        # False
print(is_valid_email_few_shot("user@.com"))            # False
print(is_valid_email_few_shot("user@domain."))         # False



# Task 5:-Prompt Tuning – Summing Digits of a Number.
# Style 1: Generic task prompt
def sum_of_digits_generic(n):
    return sum(int(digit) for digit in str(n))

# Style 2: Task + Input/Output example
def sum_of_digits_example(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

# Example Output
print(sum_of_digits_generic(123))  # ➝ 6
print(sum_of_digits_example(123))   # ➝ 6

# Short analysis
# The first style (generic task prompt) produced cleaner and more concise code using a single line with a generator expression.
# The second style (task + input/output example) is more verbose but may be easier to understand for beginners.