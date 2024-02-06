# Create a program that capitalizes the first letter of each word in a sentence
import re

def word_capitalize(sentence: str):
    words = sentence.split(" ")
    # print(words)
    new_sentence = " ".join([w.replace(w[0],w[0].upper(),1) for w in words])
    return new_sentence

def retrieve_string(message):
    error = True
    string = ""
    while error:
        try:
            string = str(input(message))
            error = False
        except ValueError as e:
            print("Only string values are valid. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the number of vowels in string. Please try again.")
    return string


def main():
    print("##### We will capitalize the first letter of each word in a sentence. #####")
    sentence = retrieve_string("Enter a sentence:")
    capitalized = word_capitalize(sentence)
    print (f"The word frequency in the sentence: '{sentence}' is:\n{capitalized}")

main()
