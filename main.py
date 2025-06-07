def main(book):
    with open(f"books/{book}") as f:
        get_book_text = f.read()
        print (get_book_text)

main("frankenstein.txt")