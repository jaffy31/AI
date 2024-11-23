#Write a Python program to generate a calendar for the given month and year without using the calendar module.


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def generate_calendar(year, month):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[2] = 29

    print(f"Calendar for {month}/{year}:\n")
    print("Mo Tu We Th Fr Sa Su")

    day_of_week = sum(days_in_month[:month]) % 7

    for _ in range(day_of_week):
        print("   ", end=" ")

    for day in range(1, days_in_month[month] + 1):
        print(f"{day:2} ", end=" ")
        day_of_week = (day_of_week + 1) % 7
        if day_of_week == 0:
            print()

if __name__ == "__main__":
    # Input: Year and Month
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    # Run the calendar generator
    generate_calendar(year, month)
