import sys
from stats import get_num_words
from stats import get_num_chars
from stats import reports

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")

    book_path = sys.argv[1]
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
