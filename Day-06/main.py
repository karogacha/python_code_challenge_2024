# Write a program to count the occurrences of a specific character in a string.

def num_occurrences(text: str, char: str):

    count = len([c for c in text.lower() if c == char.lower()])

    return count

def main():
    print("##### We will count the ocurrences of a specific character in a string. #####")
    error = True
    string = ""
    while error:
        try:
            string = str(input("Enter a string: "))
            c=''
            while len(c)!=1:
                c = str(input("Enter a character to count: "))
                if len(c)>1:
                    print("You should enter a single character to find. Pleas try again.")
            error = False
        except ValueError as e:
            print("Only string values are valid. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number of vowels in string. Please try again.")
    count = num_occurrences(string, c)
    print(f"The number times the character '{c}' occures in the string '{string}' is: {count}")


main()
