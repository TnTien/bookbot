def main():

    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = count_char(text)
    char_only = char_report(char_counts)
    print_report(char_only, num_words, book_path)
    

        
def get_book_text(book):
    with open(book) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    char_count = {}

    for i in text.lower():
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def char_report(char_count):
    abc_list = []

    for letter in char_count:
        if letter.isalpha():
            temp_dict = {}
            temp_dict["letter"] = letter
            temp_dict["num"] = char_count[letter]
            abc_list.append(temp_dict)
    abc_list.sort(reverse=True, key=sort_on)

    return abc_list

def print_report(char_only, num_words, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for dict_items in char_only:
        print(f"The '{dict_items['letter']}' character was found {dict_items['num']} times")
        
    print("--- End report ---")




main()
