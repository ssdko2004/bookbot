from stats import get_book_word_count
from stats import get_count_of_characters
from stats import sort_character_count
from sys import argv
from sys import exit

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def main():

    if (len(argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        return

    book_location = argv[1]
    book_text = get_book_text(book_location)
    word_count = get_book_word_count(book_text)
    character_count = get_count_of_characters(book_text)    
    sorted_character_count = sort_character_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_count in sorted_character_count:
        print(f"{char_count["char"]}: {char_count["count"]}")

    print("============= END ===============")



main()