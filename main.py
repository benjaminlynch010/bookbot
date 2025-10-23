from stats import get_num_words
from stats import get_num_chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count_dict = get_num_chars(text)
    print(f"Found {num_words} total words")
    print(char_count_dict)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()
