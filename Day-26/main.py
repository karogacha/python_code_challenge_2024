# Create a program that uses a lambda function to square each element of a list.

def square(num:float):
    return num * num

def retrieve_list_numbers(num=-1):
    error = True
    # Retrieve the number of elements in the list
    while error and (num == -1):
        try:
            num = int(input("Enter the number of elements: "))
            if num <= 0:
                print("The number of elements of the list has to be more than 0. Please try again.")
            else:
                error = False
        except ValueError as e:
            print("Only integer values are valid for the number of elements. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number of elements. Please try again.")
    # Retrive the elements values for the list
    i=0
    my_list = []
    while i < num:
        try:
            val = float(input(f"Enter the value No. {i+1}: "))
            my_list.append(val)
            i+=1
        except ValueError as e:
            print("Only numeric values are valid for each element. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the value for one element. Please try again.")

    return my_list

def main():
    print("##### We will square each element of a list. #####")
    list_num =retrieve_list_numbers()
    square_list = list(map(lambda x: square(x), list_num))
    print(f"Given the following lists: {list_num}, the new list with squares is: {square_list}")

main()
