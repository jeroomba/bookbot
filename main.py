import sys

from stats import get_num_words, sorted_dictionaries, unique_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def check_input():
    command = sys.argv
    if len(command) == 2:
        book_path = sys.argv[1]
        return book_path
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    path = check_input()
    file_contents = get_book_text(path)
    count = get_num_words(file_contents)
    sorted = sorted_dictionaries(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for items in sorted:
        print(f"{items['char']}: {items['num']}")
    print("============= END ===============")


main()
