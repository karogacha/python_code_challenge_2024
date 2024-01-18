# Write a program to check if a number is positive, negative, or zero.

def number_desc(num):

    result=""
    try:
        result = "positive" if num > 0 else "negative" if num < 0 else "zero"
    except ValueError:
        return None
    except Exception:
        return None

    return result

def main():
    print("##### We will chek if the number is positive, negative, or zero. #####")
    error = True
    num = 0
    # Retrieve the number
    while error:
        try:
            num = float(input("Enter the number to check: "))
            error = False
        except ValueError as e:
            print("Only numeric values are valid for the number to check. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number to check. Please try again.")
    # Retrive the elements values for the list
    res = number_desc(num)
    if res is not None:
        print(f"The number {num} is: {res}")
    else:
        print(f"Something went wrong while checking the given number.")


main()
