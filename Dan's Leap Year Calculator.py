# What is a leap year?
# What are the calculations
# How many leap years to find? 1000AD -> now inside a list
# From said list, print the ten most recent ones

def leapyear_count(start, end):
    leap_years = []
    for i in range(start, end):
        if i % 100 == 0 and i % 400 == 0:
            leap_years.append(i)
        else:
            if i % 4 == 0:
                leap_years.append(i)
    print(leap_years[-10:])


print("Dan's Leap Year Calculator")
print("Welcome user! For starters, what IS a leap year?"
      "A leap year is a year that has 366 days instead of the usual 365.\n The extra day - February 29th -"
      " is is added to keep our calendar in sync with the Earth's orbit around the Sun.")

start = input("What is your start year?")
end = input("What is your end year?")

leapyear_count(int(start), int(end))
