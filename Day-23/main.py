# Write a program that checks if a key exists in a dictionary.

def check_key(dict, key):
    return True if key in dict else False

def retrieve_dictionary(num=-1):
    error = True
    # Retrieve the number of elements in the dictionary
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
    my_dict = {}
    while i < num:
        try:
            k = str(input(f"Enter the key No. {i+1}: "))
            val = input(f"Enter the value No. {i+1}: ")
            my_dict[k] = val
            i+=1
        except ValueError as e:
            print("Only string values are valid for each element. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the value for one element. Please try again.")

    return my_dict


def main():
    print("##### We will check if a key exists in a dictionary. #####")
    my_dict=retrieve_dictionary()
    k = str(input("Enter the key to search: "))
    print(f"The given key '{k}' {'' if check_key(my_dict, k) else 'does not '}exists in the given dictionary: {my_dict}")

main()
