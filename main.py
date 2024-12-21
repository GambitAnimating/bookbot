def main():
    book_path = "books/frankenstein.txt"
    get_book_report(book_path)

def sort_on(dict):
    return dict["num"]

def get_book_report(book_path):
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_characters_dict = get_num_characters(book_text)
    print(f"--- Begin report of {book_path} ---")
    print (f"{num_words} words found in the document")
    dict_list = []
    for char in num_characters_dict:
        dict_list.append({"char": char, "num":num_characters_dict[char]})
    
    dict_list.sort(reverse=True, key=sort_on)

    for local_dict in dict_list:
        print(f"The {local_dict["char"]} character was found {local_dict["num"]} times")

    print("--- End report ---")
    
    

def get_num_characters(text):
    char_dict = {}

    for char in text:
        lowercase_char = str.lower(char)
        if (lowercase_char not in char_dict):
            char_dict[lowercase_char] = 1
        else:
            char_dict[lowercase_char] += 1

    return char_dict

def get_num_words(text):
    return len(text.split())

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
main()