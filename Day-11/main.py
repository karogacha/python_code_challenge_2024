# Write a program to print the multiplication table of a given number.

def multiplication_table(num, line=1, table=""):

    if line == 11:
        return table
    result_line = f'\n╟───────────────────┼──────────╢'
    result_line +=f'\n║ {num:>7} x {line:<7} | {num * (line):>8} ║'
    if(line == 1):
        # First line of the table
        table +=f'\n╔═══════════════════╤══════════╗'
        table +=f'\n║  Multiplication   | Result   ║'
        table += result_line
    elif(line == 10):
        # Last line of the table
        table += result_line
        table +=f'\n╚═══════════════════╧══════════╝\n'
    else:
        table +=result_line
    # print(table)
    return multiplication_table(num, line+1 ,table)
    # return table

def main():
    print("##### We will print the multiplication table of a given number. #####")
    error = True
    num = 0
    # Retrieve the number
    while error:
        try:
            num = int(input("Enter a number: "))
            if num>9999999:
                print("The number must be less than 10,000,000. Please try again.")
            else:
                error = False
        except ValueError as e:
            print("Only integer values are valid for the number to check. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number to check. Please try again.")
    # Retrive the elements values for the list
    res = multiplication_table(num)
    if res is not None:
        print(f"The multiplication table for {num} is: \n{res}.")
    else:
        print(f"Something went wrong while checking the given number.")


main()
