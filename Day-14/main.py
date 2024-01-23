# Write a program to print the first n numbers of a Fibonacci sequence

def fibonacci_seq(num: int, fib_seq=[]):

    if num==0:
        return fib_seq
    else:
        fib_seq.append(0 if len(fib_seq)==0 else 1 if len(fib_seq)==1 else fib_seq[-1]+fib_seq[-2])
        return fibonacci_seq(num-1, fib_seq)

def retrieve_num():
    error = True
    num = 0
    # Retrieve the number
    while error:
        try:
            num = int(input("Enter a number: "))
            if num>9999999:
                print("The number must be less than 10,000,000. Please try again.")
            elif num<2:
                print("The number must be more or equal than 2. Please try again.")
            else:
                error = False
        except ValueError as e:
            print("Only integer values are valid for the number. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number. Please try again.")
    return num

def main():
    print("##### We will print the first n numbers of a Fibonacci sequence. #####")
    num = retrieve_num()
    fib = fibonacci_seq(num)
    print(f"The Fibonacci sequence for the first '{num}' numbers is: '{fib}'")


main()
