# Create a program that sorts a list of strings alphabetically.

# solved using algorithm, we can use sort and the result is the same.
def sorted(my_list):
    sorted_list=[]
    for elem in my_list:
        index=0
        inserted = False
        for index, value in enumerate(sorted_list):
            if elem < value:
                sorted_list.insert(index,elem)
                inserted=True
                break
        if not inserted: sorted_list.append(elem)
    return sorted_list


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
    print("##### We will order a list of string alphabetically. #####")
    list_1 =retrieve_list()
    new_list = sorted(list_1)
    print(f"Given the following list: {list_1}, the sorted list is: {new_list}")

main()
