#Task-1(Prime number check without using functions).
# Program to check if a number is prime or not

num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number")
else:
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

#---------------------------------------------------------------------------------------

#Task-2 (optimize the above code).
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")



