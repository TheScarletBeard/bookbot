import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_location = sys.argv[1]

def main():
    book_path = book_location
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    
    char_list = get_list_chars(num_chars)
    char_list.sort(reverse=True, key=sort_chars)
    
    print("=========== BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in char_list:
        print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import (
get_num_words,
get_num_chars,
get_list_chars,
sort_chars
)

main()