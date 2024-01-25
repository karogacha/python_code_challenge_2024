# Create a program that checks if a year is a leap year.
import re
import calendar

"""A year is a leap year if the following conditions are satisfied:
The year is multiple of 400.
The year is a multiple of 4 and not a multiple of 100.
"""
def is_leap(year: int):
    if year % 400 == 0:
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False

def retrieve_year():
    error = True
    year = 0
    # Retrieve the year
    while error:
        try:
            str_year = input("Enter the Year to validate (four digits): ")
            if not re.findall(r'^\d{4}',str_year):
                print("The year must be a four digits number. Please try again.")
            else:
                year = int(str_year)
                error = False
        except ValueError as e:
            print("Only integer values are valid for the year. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number. Please try again.")
    return year

def main():
    print("##### We will check if a year is leap or not. #####")
    year = retrieve_year()
    print(calendar.calendar(year))
    print (f"With calendar.isleap() - The year {year} is", "leap." if calendar.isleap(year) else "NOT leap.")
    print (f"With formulas - The year {year} is", "leap." if is_leap(year) else "NOT leap.")


main()
