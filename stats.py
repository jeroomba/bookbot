def get_num_words(book_text):
    words_in_book = book_text.split()
    count = len(words_in_book)
    return count


def unique_count(book_text):
    lower_book_text = book_text.lower()
    unique_letters = {}
    for letter in lower_book_text:
        if letter in unique_letters:
            unique_letters[letter] += 1
        else:
            unique_letters[letter] = 1
    return unique_letters


def sort_on(items):
    return items["num"]


def sorted_dictionaries(book_text):
    single_dictionary = unique_count(book_text)
    pair_dictionary = []
    for letter in single_dictionary:
        if letter.isalpha():
            pair_dictionary.append({"char": letter, "num": single_dictionary[letter]})
    pair_dictionary.sort(reverse=True, key=sort_on)
    return pair_dictionary


# Test to check sync
