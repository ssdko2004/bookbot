def get_book_word_count(book_text):
    return len(book_text.split())

def get_count_of_characters(text):
    counts = {}
    for character in text:        
        lowered_char = character.lower()
        if lowered_char not in counts:
            counts[lowered_char] = 0

        counts[lowered_char] += 1

    return counts


def sort_character_count(character_counts):
    sorted_character_counts = []

    for char in character_counts:
        if not (char.isalpha()):
            continue

        sorted_character_counts.append({"char": char, "count": character_counts[char]})

    def sort_on(item):
        return item["count"]
    
    sorted_character_counts.sort(reverse=True, key=sort_on)
    return sorted_character_counts
