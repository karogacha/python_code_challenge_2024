# Write a function that counts the frequency of each word in a sentence.
import re

def word_freq(sentence: str):
    words = re.findall(r"[\w']+",sentence.lower())
    # print(words)
    words_fq={}
    for w in words:
        if len(words_fq) == 0:
            words_fq[w] = 1
        else:
            # print(len(words_fq))
            if w in words_fq:
                words_fq[w] += 1
            else:
                words_fq[w] = 1
    return words_fq

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
    print("##### We will count the frequency of each word in a sentence. #####")
    sentence = retrieve_string()
    frequency = word_freq(sentence)
    print (f"The word frequency in the sentence: '{sentence}' is:\n{frequency}")

main()
