# Create a program that swaps the values of two variables
def swap_variables(v1, v2):
    temp = v1
    # assign the value of var2 into variable 1
    v1 = v2
    # assign the value of var1 into variable 2
    v2 = temp

    return v1, v2

def main():
    print("Enter your first variable:")
    var1 = input()
    print("Enter your second variable:")
    var2 = input()
    print(f"Values:\n\tFirst variable:{var1}\n\tSecond variable:{var2}")
    var1, var2 = swap_variables(var1, var2)
    print(f"Swapped values:\n\tFirst variable:{var1}\n\tSecond variable:{var2}")

main()
