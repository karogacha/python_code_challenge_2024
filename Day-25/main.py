# Create a program to concatenate two lists.

def concat_lists(first, second):
    return first + second

def retrieve_list(num=-1):
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
            val = input(f"Enter the value No. {i+1}: ")
            my_list.append(val)
            i+=1
        except Exception as e:
            print("An unexpected error ocurred while retreiving the value for one element. Please try again.")

    return my_list

def main():
    print("##### We will find the largest among three numbers. #####")
    print("List #1")
    list_1 =retrieve_list()
    print("List #2")
    list_2 = retrieve_list()
    new_list = concat_lists(list_1, list_2)
    print(f"Given the following lists \n\t#1: {list_1}\n\t#2: {list_2}")
    print(f"The resulting list is: {new_list}")

main()
