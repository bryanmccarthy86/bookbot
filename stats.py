def get_num_words(book):
    with open(f"{book}") as f:
        get_book_text = f.read()
#        print (get_book_text)
        book_array = get_book_text.split()
        num_of_words = len(book_array)
        print(f"Found {num_of_words} total words")

def count_letters(book):
    with open(f"{book}") as f:
        get_book_text = f.read()
        lower_text = get_book_text.lower()
        characters = list(set(lower_text))
        #print(lower_text)
        dict = {}
        for letters in characters:
           count = lower_text.count(letters)
           dict[letters] = count
        #print (dict)
        sorted_words= sorted(dict.items(), key=lambda item: int(item[1]), reverse=True)
        #print(sorted_words)
        for k,v in sorted_words:
            if k.isalpha():
                print(f"{k}: {v}")
        

#count_letters('frankenstein.txt')