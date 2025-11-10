from stats import get_word_count, letter_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    count = get_word_count(text)
    lettercount = letter_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for key, value in lettercount.items():
        if key.isalpha():
            print(f"{key}: {value}")
        else:
            continue
    print("============= END ===============")

if __name__ == "__main__":
    main()
