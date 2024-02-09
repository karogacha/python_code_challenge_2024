# Create a function that finds the second smallest element in a list.

def second_smallest_number(elem):
    smallest=elem[0]
    second_smallest = elem[0]
    for e in elem:
        if smallest>=e:
            second_smallest=smallest
            smallest=e
        elif second_smallest>=e:
            second_smallest=e
    return second_smallest

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
    print("##### We will find the second-smallest among three numbers. #####")
    my_list=retrieve_list_numbers()
    num_min = second_smallest_number(my_list)
    print(f"Given the following list {my_list}, the second-smallest number is: {num_min}")

main()
