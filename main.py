import sys

from stats import get_num_words, get_char_count, sort_by_count


def main(book_path):
    '''
    The main function: calls the required function to collect the 
    neccesary data and prints the report.
    '''

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)
    word_count = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    chars_count = sort_by_count(get_char_count(text))
    for item in chars_count:
        for k, v in item.items():
            if k.isalpha():
                print(f"{k}: {v}")
    
    print("============= END ===============")


def get_book_text(path):
    '''
    This function reads text from file using given path to file,
    and returns the text extracted.'''
    
    with open(path) as f:
        return f.read()


if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])
