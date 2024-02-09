# Create a program that removes the nth element from a list.

'''
different ways to remove the nth element from a list:
1. use the built-in del statement (imperative way)
2. use the built-in pop() method
3. use the built-in remove() method
4. use slicing (pythonic way)
5. use a list comprehension (pythonic way)
6. use the built-in filter() function (functional way)
7. use shifting and overwriting in-place (imperative way)
'''
def remove_element(my_list, index):
    return [val for i,val in enumerate(my_list) if i!=index-1]

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

def retrieve_num(max=10000000):
    error = True
    num = 0
    # Retrieve the number
    while error:
        try:
            num = int(input("Enter the index to remove: "))
            if num>max:
                print(f"The number must be less or equal than {max}. Please try again.")
            elif num<0:
                print("The number must be more or equal than 1. Please try again.")
            else:
                error = False
        except ValueError as e:
            print("Only integer values are valid for the number. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number. Please try again.")
    return num

def main():
    print("##### We will remove the nth element of a given list. #####")
    list_1 =retrieve_list()
    index = retrieve_num(len(list_1))
    new_list = remove_element(list_1, index)
    print(f"Given the following list: {list_1}. When we remove the {index}th elemet, the resulting list is: {new_list}")

main()
