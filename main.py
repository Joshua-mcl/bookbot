def readfile():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return file_contents

def count_words(file_contents):
    words = file_contents.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
def sort_on(d):
    return d["num"]

def charts_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



def main():
    file_contents = readfile()
    num_words = count_words(file_contents)
    chars_dict = get_chars_dict(file_contents)
    chars_sorted_list = charts_dict_to_sorted_list(chars_dict)
    
    print(f"--- Begin report of frankenstien ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")


if __name__ == "__main__":
    main()
    


