def fizzBuzz(number):
    number = int(number)
    message = ''
    if number % 3 == 0:
        message += 'Fizz'
    if number % 5 == 0:
        message += 'Buzz'
    if message == '':
        return number
    return message

user_number = input('Please enter a number: ')
while user_number != '':
    print(fizzBuzz(user_number))
    user_number = input('Please enter a number: ')
