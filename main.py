def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(num_words_in_str(file_contents))

def num_words_in_str(text: str):
    words = text.split()
    return len(words)

main()
