from stats import get_num_words, count_letters
import sys

def create_count(book):
    new_dict = {}
  #  with open(f"books/{book}") as f:


def main(book):
    with open(f"{book}") as f:
        get_book_text = f.read()
        #print (get_book_text)
        lower_case = get_book_text.lower()
        #print(lower_case)

        # get_book_text.split()


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    get_num_words(sys.argv[1])
    count_letters(sys.argv[1])
