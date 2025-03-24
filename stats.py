def get_word_number(text):
    words = text.split()
    return len(words)

def count_character(text):
    book = text.lower()
    character = {}
    for letter in book:
        if letter in character:
            character[letter] += 1
        else:
            character[letter] = 1
    return character

def character_list(dictio):
    char_list = []
    for char, count in dictio.items():
        char_list.append({"char": char, "count": count})
    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list