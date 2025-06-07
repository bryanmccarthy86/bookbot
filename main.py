from stats import get_num_words, count_letters

def create_count(book):
    new_dict = {}
  #  with open(f"books/{book}") as f:


def main(book):
    with open(f"books/{book}") as f:
        get_book_text = f.read()
        #print (get_book_text)
        lower_case = get_book_text.lower()
        #print(lower_case)

        # get_book_text.split()



get_num_words("frankenstein.txt")
count_letters("frankenstein.txt")