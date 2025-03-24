import sys

def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents

from stats import get_word_number

from stats import count_character

from stats import character_list


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else :
        book_path = sys.argv[1]
    path = book_path
    text = get_book_text(path)
    word_count = get_word_number(text)
    character_count = count_character(text)
    book_character = character_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path} ...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character_count in book_character:
        char = character_count["char"]
        count = character_count["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()