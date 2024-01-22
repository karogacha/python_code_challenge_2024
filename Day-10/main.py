# Write a program to remove duplicates from a list.

def remove_duplicates(elem):

    return list(set(elem))

def main():
    print("##### We will get the max value of a given list of values. #####")
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
            val = input(f"Enter the value No. {i+1}: ")
            my_list.append(val)
            i+=1
        except ValueError as e:
            print("Only float values are valid for each element. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the value for one element. Please try again.")

    new_list = remove_duplicates(my_list)
    print(f"Given the following list {my_list}, the resulting list without duplicates is: {new_list}")

main()
