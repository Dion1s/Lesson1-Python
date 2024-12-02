import datetime
#(BASED)
# Завдання 1.1
CURRENT_YEAR = 2024  # Поточний рік як константа

birth_year = int(input("Enter your year of birth: "))
age = CURRENT_YEAR - birth_year
print(f"For you {age} years.")

# Завдання 1.2
flash_drive_gb = float(input("Enter the size of the flash drive in GB: "))
file_size_mb = 820 

flash_drive_mb = flash_drive_gb * 1024

num_files = flash_drive_mb // file_size_mb
print(f"A flash drive with a capacity of {flash_drive_gb} GB can hold {int(num_files)} files of size {file_size_mb} MB.")

# Завдання 2.1
digit = int(input("Enter a number from 0 to 9: "))

match digit:
    case 1:
        print("!")
    case 2:
        print("@")
    case 3:
        print("#")
    case 4:
        print("$")
    case 5:
        print("%")
    case 6:
        print("^")
    case 7:
        print("&")
    case 8:
        print("*")
    case 9:
        print("(")
    case 0:
        print(")")
    case _:
        print("Incorrect input.")

# Завдання 2.2
year = int(input("Enter the year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("This year is a leap year.")
else:
    print("This year is not a leap year.")

# Завдання 2.3


day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

current_date = datetime.date(year, month, day)
next_day = current_date + datetime.timedelta(days=1)

print(f"Next date: {next_day}")

# Завдання 3.1
start = int(input("Enter the beginning of the range: "))
end = int(input("Type the end of the range: "))

sum_of_numbers = 0
for number in range(start, end + 1):
    sum_of_numbers += number

print(f"The sum of numbers in the range from {start} to {end}: {sum_of_numbers}")

# Завдання 3.2
number = int(input("Enter a number: "))
count = 0

while number != 0:
    number //= 10
    count += 1

print(f"The number of digits in a number: {count}")

# Завдання 3.3
positive = 0
negative = 0
zero = 0
even = 0
odd = 0

for _ in range(10):
    number = int(input("Enter a number: "))
    
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1
    
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Positive: {positive}, Negative: {negative}, Zero: {zero}")
print(f"Even: {even}, Odd: {odd}")

# Завдання 3.4
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

index = datetime.datetime.now().weekday()

while True:
    print(f"Day of the week: {days_of_week[index]}")
    answer = input("Would you like to see the next day? (YES/NO): ").strip().lower()
    
    if answer != "yes":
        break
    
    index = (index + 1) % 7  