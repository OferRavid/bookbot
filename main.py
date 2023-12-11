import string
import sys


def main():
    '''
    The main function: calls the required function to collect the 
    neccesary data and prints the report.
    '''

    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---\n")
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document.\n")
    char_dict = get_char_count(text)
    sorted_chars = sorted([k for k in char_dict.keys()])
    for char in sorted_chars:
        print(f"The '{char}' character was found {char_dict[char]} times.")
    print("\n--- End report ---")


def get_word_count(text: str):
    '''
    This function calculates and returns the word count in given text.
    '''

    words = text.split()
    return len(words)

def get_char_count(text: str):
    '''
    This function counts appearances of letters in given text,
    and returns a dictionary of letter(lowercase):count.
    '''

    char_dict = dict((char, 0) for char in list(string.ascii_lowercase))
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in char_dict:
            char_dict[char] += 1
    return char_dict

def get_book_text(path):
    '''
    This function reads text from file using given path to file,
    and returns the text extracted.'''
    
    with open(path) as f:
        return f.read()


main()

