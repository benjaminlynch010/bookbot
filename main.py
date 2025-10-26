from stats import get_num_words
from stats import get_num_chars
from stats import reports

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count_dict = get_num_chars(text)
    sorted = reports(char_count_dict)
    print(f"Found {num_words} total words")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()
