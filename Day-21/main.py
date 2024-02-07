# Create a program to remove a specific element from a set.

def remove_set(my_set, elem):
    temp_set= set()
    temp_set.add(elem)
    return my_set.difference(temp_set)

def retrieve_string(message):
    error = True
    string = ""
    while error:
        try:
            string = str(input(message))
            error = False
        except ValueError as e:
            print("Only string values are valid. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number of vowels in string. Please try again.")
    return string

def retrieve_set(num=-1):
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
    my_set = set()
    while i < num:
        try:
            val = str(input(f"Enter the value No. {i+1}: "))
            my_set.add(val)
            i+=1
        except ValueError as e:
            print("Only string values are valid for each element. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the value for one element. Please try again.")

    return my_set

def main():
    print("##### We will take a list of numbers and return a new list containing only the even numbers. #####")
    set_elem = retrieve_set()
    my_elem = retrieve_string("Enter the element to remove: ")
    new_set = remove_set(set_elem, my_elem)
    print(f"Given the following set: {set_elem} and the element '{my_elem}'\nThe returning set without the element is: {new_set}")


main()
