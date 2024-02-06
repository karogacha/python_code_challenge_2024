# Write a function to calculate the factorial of a number.

def factorial(num: int, res=1):

    if num==1:
        return res
    else:
        res=res*num
        return factorial(num-1, res)

def retrieve_num():
    error = True
    num = 0
    # Retrieve the number
    while error:
        try:
            num = int(input("Enter a number: "))
            if num>9999999:
                print("The number must be less than 10,000,000. Please try again.")
            elif num<1:
                print("The number must be more or equal than 1. Please try again.")
            else:
                error = False
        except ValueError as e:
            print("Only integer values are valid for the number. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number. Please try again.")
    return num

def main():
    print("##### We will calculate the Factorial of a number. #####")
    num = retrieve_num()
    fac_num = factorial(num)
    print(f"The Factorial of '{num}' is: '{fac_num}'")


main()
