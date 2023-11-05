

"""

    this series is the number serie which contains all the interger whose digitsum is fully
    devide that number 

"""

rows = int(input("Enter no of rows : "))

num = 1;

for i in range(rows):

    for j in range(rows):

        digitsum = 0;
        num1 = num

        while(num1 > 0):
            
            digitsum += (num1 % 10);
            num1 //= 10

        if(num % digitsum == 0):
            print(num, end=  " ")
        
        num += 1

    print()



# # Define a function to check if a number is a Niven number
# def is_niven_number(number):
#     digit_sum = sum(int(digit) for digit in str(number))
#     return number % digit_sum == 0

# # Set the number of rows
# rows = 4

# # Initialize variables for generating Niven numbers
# niven_numbers = []
# current_number = 1

# # Generate Niven numbers and store them in the niven_numbers list
# while len(niven_numbers) < rows ** 2:
#     if is_niven_number(current_number):
#         niven_numbers.append(current_number)
#     current_number += 1

# # Print Niven numbers in a square pattern
# for i in range(rows):
#     for j in range(rows):
#         print(niven_numbers[i * rows + j], end=" ")
#     print()


