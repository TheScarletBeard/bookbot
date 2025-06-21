def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def get_list_chars(chars_dict):
    char_list = []
    for char in chars_dict:
        if char.isalpha():
            count = chars_dict[char]
            new_dict = {"char":char,"num":count}
            char_list.append(new_dict)
    return char_list

def sort_chars(chars):
    return chars["num"]
        