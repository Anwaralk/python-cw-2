first_number = int(input('enter first number: '))
second_number = int(input('enter second number: '))
operation = input('choose operation: ')

if operation == '+':
    print(f'{first_number} + {second_number} = {first_number+second_number}')
elif operation == '-':
    print(f'{first_number} - {second_number} = {first_number-second_number}')
elif operation == '*':
    print(f'{first_number} * {second_number} = {first_number*second_number}')
elif operation == '/':
    print(f'{first_number} / {second_number} = {first_number/second_number}')
else: 
    print('invalid input')

