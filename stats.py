def get_num_words(text: str):
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

    lowercase_text = text.lower()
    char_dict = dict((char, 0) for char in set(lowercase_text))
    for char in lowercase_text:
        char_dict[char] += 1
    return char_dict


def chars_dict_to_sorted_list(chars: dict):
    '''
    This function takes a dictionary of letter(lowercase):count, converts it to a
    list of dictionaries each a single (letter(lowercase), count) pair, and then 
    sorts it from highest to lowest based on count.
    '''

    char_list = []
    for k, v in chars.items():
        char_list.append({k: v})

    def sort_on(dict: dict):
        for k in dict.keys():
            return dict[k]
        
    return sorted(char_list, key=lambda item: sort_on(item), reverse=True)
