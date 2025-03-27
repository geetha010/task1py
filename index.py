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

#palindrom for number
num1=1221
temp=num1
rev=0
while temp>0:
    rem=temp%10
    rev=(rev*10)+rem
    temp=temp//10
if num1==rev:
    print("palindrome")
else:
    print("not a palindrome")

#user to enter a number until they enter a negitive number use a infinite while loop
while True:
    num=int(input("enter non positive number"))
    if num<0:
        print("rules neglected")
        break
    #-----------or--------#
    num1=int(input("enter a non negitive number"))
    while num1>=0:
        print(num1)
        num1=int(input("enter non negitive number"))

#fibonnacci

num1,num2=0,1
n=20
for i in range(0,20):
    num1,num2=num2,num1+num2


#implement a basic login system where the user has three attempts to enter the correct using a loop
db_username = "admin"
db_password = "password12"
attempts = 3

for attempt in range(attempts):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == db_username and password == db_password:
        print("Login successful")
        break  # Exit the loop if login is successful
    else:
        remaining_attempts = attempts - (attempt + 1)
        if remaining_attempts > 0:
            print(f"Attempt failed. Attempts left: {remaining_attempts}")
        else:
            print("Access denied")

#Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
 
def square(num):  
    return num ** 2  

def cube(num):  
    return num ** 3  

def main():  
    while True:  
        print("menu: ")  
        print("1. Square of number")  
        print("2. Cube of number")  
        print("3. Exit")  
        choice = input("Enter choice (1-3): ")  
        
        if choice == '1':  
            num = float(input("Enter a number: "))  
            print(f"Square of {num} is {square(num)}")  
        
        elif choice == '2':  
            num = float(input("Enter a number: "))  
            print(f"Cube of {num} is {cube(num)}")  
        
        else: 
            print("Exiting the program.")  
            break  

if __name__ == "__main__":  
    main()  

       


