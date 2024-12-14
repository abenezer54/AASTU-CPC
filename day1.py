# Read input n
n = int(input())

# If n is 1, the last two digits of 5^1 are 05, otherwise they are 25 for n >= 2
if n == 1:
    print(5)  # Last two digits of 5^1
else:
    print(25)  # Last two digits of 5^n for n >= 2
