import sys

from stats import get_num_words, get_char_count, chars_dict_to_sorted_list


def main():
    '''
    The main function: calls the required function to collect the 
    neccesary data and prints the report.
    '''

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)

    print_report(
        book_path,
        get_num_words(text),
        chars_dict_to_sorted_list(get_char_count(text))
    )


def get_book_text(path):
    '''
    This function reads text from file using given path to file,
    and returns the text extracted.
    '''
    
    with open(path) as f:
        return f.read()


def print_report(book_path, word_count, chars_dict_list):
    '''
    Prints the report of stats extracted from the given book.
    '''

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in chars_dict_list:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")
    
    print("============= END ===============")



if __name__=="__main__":
    main()
