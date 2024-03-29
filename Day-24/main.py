# Write a program to remove vowels from a given string.
import re

def remove_vowels(sentence: str):
    new_sent = ''.join(re.findall(r"[^aeiouAEIOU]", sentence))
    return new_sent

def replace_vowels(sentence: str):
    new_sent = ''.join([c if c.lower() not in 'aeiou' else '_' for c in sentence ])
    return new_sent

def retrieve_string():
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
    return string


def main():
    print("##### We will remove the vowels of a given string. #####")
    sentence = retrieve_string()
    new_sent = remove_vowels(sentence)
    print (f"Given the following string: '{sentence}' the resulting string without vowels is:\n{new_sent}")

main()
