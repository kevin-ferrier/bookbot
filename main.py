def count_words(book: str) -> int:
    return len(str.split(book))

def count_characters(book: str) -> dict[str, int]:
    result: dict[str, int] = {}
    for c in book:
        if not c.isalpha():
            continue

        character = c.lower()
        if character not in result:
            result[character] = 1
        else:
            result[character] += 1

    return result

def report(book_path: str) -> None:
    print(f"--- Begin report of {book_path} ---")

    with open(book_path) as f:
        content = f.read()
        print(f"{count_words(content)} words found in the document\n")

        characters = list(count_characters(content).items())
        characters.sort(key=lambda item: item[1], reverse=True)
        for combination in characters:
            print(f"The '{combination[0]}' character was found {combination[1]} times")

    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    report(book_path=book_path)

if __name__ == "__main__":
    main()
