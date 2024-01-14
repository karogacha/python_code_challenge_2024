# Write a function to count the number of vowels in a given string

def num_vowels(text: str):
    vowels = ['a','e','i','o','u']

    count = len([c for c in text if c in vowels])

    return count

def main():
    print("##### We will count the number of vowels given a string. #####")
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
    num_v = num_vowels(string)
    print(f"The number of vowels in the string '{string}' is: {num_v}")


main()
