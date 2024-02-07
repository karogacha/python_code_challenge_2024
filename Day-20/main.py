# Write a function that takes a list of numbers and returns a new list containing only the even numbers.

def is_even(num):
    return True if num % 2 == 0 else False

def list_even(elem):
    return [e for e in elem if is_even(e)]

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
            val = int(input(f"Enter the value No. {i+1}: "))
            my_list.append(val)
            i+=1
        except ValueError as e:
            print("Only integer values are valid for each element. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the value for one element. Please try again.")

    return my_list

def main():
    print("##### We will take a list of numbers and return a new list containing only the even numbers. #####")
    list_numbers = retrieve_list_numbers()
    new_list = list_even(list_numbers)
    print(f"Given the following list of numbers: {list_numbers}\nThe returning list of even numbers is: {new_list}")


main()
