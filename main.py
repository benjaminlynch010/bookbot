def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    word_count = count_words(text)
    print(f"{word_count} words found in the document")
    char_dict = count_char(text)
    print(char_dict)

def count_char(text):
    chars = {}
    for c in text:
        lowercase = c.lower()
        if lowercase in chars:
            chars[lowercase] += 1
        else: chars[lowercase] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

main()
