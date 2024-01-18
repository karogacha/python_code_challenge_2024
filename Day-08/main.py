# Write a function that accepts a string and calculates the number of uppercase
# and lowercase letters in it.
import re

def num_case(text: str):
    uppercase = re.findall("[A-Z]",text)
    lowercase = re.findall("[a-z]",text)
    return len(uppercase), len(lowercase)

def main():
    print("##### We will calculate the number of uppercase and lowercase in the given a string. #####")
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
    up, low = num_case(string)
    print(f"Given the string '{string}'\n\t- The number of uppercase letters is: {up}\n\t- The number of lowercase letters is: {low}")


main()
