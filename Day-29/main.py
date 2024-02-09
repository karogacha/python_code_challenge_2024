# Create a function that generates a random number between a given range.
import random

def random_num(min, max):
    return random.randint(min, max)


def retrieve_num(min=-10000000,max=10000000):
    error = True
    num = 0
    # Retrieve the number
    while error:
        try:
            num = int(input("Enter the index to remove: "))
            if num>max:
                print(f"The number must be less or equal than {max}. Please try again.")
            elif num<min:
                print(f"The number must be more or equal than {min}. Please try again.")
            else:
                error = False
        except ValueError as e:
            print("Only integer values are valid for the number. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number. Please try again.")
    return num

def main():
    print("##### We will remove the nth element of a given list. #####")
    min = retrieve_num()
    max = retrieve_num(min=min)
    num = random_num(min, max)
    print(f"Given the following range: {min}-{max}. The random number generated is: {num}")

main()
