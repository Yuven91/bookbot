from stats import get_word_count, letter_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    count = get_word_count(text)
    lettercount = letter_count(text)
    print(lettercount)
    print(f"Found {count} total words")

if __name__ == "__main__":
    main()
