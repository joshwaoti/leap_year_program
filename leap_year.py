'''
a leap year among other properties, is divisible by 100 and or by 4
this two properties are enough to determine wether a year is a leap year
'''

year = int(input("Write the year you want to check in numbers. \nYEAR: "))

if year % 100 == 0:
    print(f"{year} is a leap year.")

elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f" {year} is not a leap year ")



