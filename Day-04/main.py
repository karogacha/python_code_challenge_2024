# Write a program to find the sum of all elements in a list.

def sum_elements(elem):

    try:
        result = 0
        for e in elem:
            result += float(e)
    except ValueError:
        return None
    except Exception:
        return None

    return result

def main():
    print("##### We will calculate the sum of all the elements in a given list. #####")
    error = True
    num = 0
    # Retrieve the number of elements in the list
    while error:
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
            print("Only float values are valid for each element. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the value for one element. Please try again.")

    sum = sum_elements(my_list)
    if sum is not None:
        print(f"The sum of the elements in the list [{my_list}] is: {sum}")
    else:
        print(f"Something went wrong while calculating the sum of the given list.")


main()
