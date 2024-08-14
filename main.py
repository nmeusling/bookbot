def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print_report(file_contents)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_counts = {}
    for char in text:
        if not char.isalpha():
            continue
        char = char.lower()
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def print_report(text):
    word_count = count_words(text)
    character_count = count_characters(text)
    sorted_char_count = dict(sorted(character_count.items(), reverse=True, key=lambda item: item[1]))
    print("Report for frankenstein")
    print(f"{word_count} words found in document")
    print()
    for k, v in sorted_char_count.items():
        print(f"The {k} character was found {v} times")


main()