# Write a program to check if a number is even or odd.

def even_or_odd(num):

    result=""
    try:
        result = "even" if num % 2 == 0 else "odd"
    except ValueError:
        return None
    except Exception:
        return None

    return result

def main():
    print("##### We will chek if the number is even or odd. #####")
    error = True
    num = 0
    # Retrieve the number
    while error:
        try:
            num = int(input("Enter the number to check: "))
            error = False
        except ValueError as e:
            print("Only integer values are valid for the number to check. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number to check. Please try again.")
    # Retrive the elements values for the list
    res = even_or_odd(num)
    if res is not None:
        print(f"The number {num} is {res}.")
    else:
        print(f"Something went wrong while checking the given number.")


main()
