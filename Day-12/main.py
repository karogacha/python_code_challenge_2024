# Write a program to reverse a given string.

def reverse_string(text: str, reversed: str=""):

    if len(text)==0:
        # print(reversed)
        return reversed
    else:
        return reverse_string(text[:-1],reversed + text[-1])

def main():
    print("##### We will count the ocurrences of a specific character in a string. #####")
    error = True
    string = ""
    while error:
        try:
            string = str(input("Enter a string: "))
            error = False
        except ValueError as e:
            print("Only string values are valid. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number of vowels in string. Please try again.")
    rev = reverse_string(string, )
    print(f"The given string is '{string}' and reversed: '{rev}'")


main()
