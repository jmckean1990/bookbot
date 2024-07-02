def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
        words = count_words(file_contents)
        character_dict = count_characters(file_contents)
        character_data = [{"character" : character, "count" : character_dict[character]} for character in character_dict]
        character_data.sort(key=lambda char_dict:char_dict["count"], reverse=True)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        print()
        for entry in character_data:
            if entry["character"].isalpha():
                print(f"The {entry['character']} character was found {entry['count']} times")

def count_words(text):
    return len(text.split())

def count_characters(text):
    lowercase_text = text.lower()
    character_dict = {}
    
    for character in lowercase_text:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    
    return character_dict
    


if __name__ == "__main__":
    main()