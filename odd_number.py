# Function to check if a number is odd
def is_odd(num):
    return num % 2 != 0

# Loop through the range and print odd numbers
for number in range(200, 301):
    if is_odd(number):
        print(number)

##new comment using push command