#Lambda and Happy numbers
def check_happy_number(check_function):
    try:
        number = int(input("Enter the number: "))
        if check_function(number):
            print("Happy number")
        else:
            print("Bad number Here's a quote: 'Happiness is a state of mind, not a number.")
    except ValueError:
        print("Please enter the correct number.")

check_happy_number(lambda num: sum(int(digit) for digit in str(num)) % 2 == 0)

def calculate(a, b, operation):
    return operation(a, b)

print("Calculatina ADD")
print(calculate(10, 5, lambda x, y: x + y))

print("Calculatina SUB")
print(calculate(10, 5, lambda x, y: x - y)) 

print("Calculatina MULTY")
print(calculate(10, 5, lambda x, y: x * y))

print("Calculatina DIV")
print(calculate(10, 0, lambda x, y: x / y if y != 0 else "Diveded by zero"))  




