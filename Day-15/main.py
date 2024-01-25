# Create a program that checks if a year is a leap year.
import re
import calendar

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
    print (f"The year {year} is", "leap." if calendar.isleap(year) else "NOT leap.")
    print(calendar.calendar(year))


main()
