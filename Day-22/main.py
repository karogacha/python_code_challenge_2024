# Create a program to find the second-largest element in a list.

def second_largest_number(elem):
    largest=elem[0]
    second_largest = elem[0]
    for e in elem:
        if largest<=e:
            second_largest=largest
            largest=e
        elif second_largest<=e:
            second_largest=e
    return second_largest

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
    print("##### We will find the largest among three numbers. #####")
    my_list=retrieve_list_numbers()
    num_max = second_largest_number(my_list)
    print(f"Given the following list {my_list}, the second-largest number is: {num_max}")

main()
