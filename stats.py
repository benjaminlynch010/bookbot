def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict


def sort_on(items):
    return items["count"]

def reports(dict):
    char_list = []
    for item in dict:
        entry = { "char": item, "count": dict[item] }
        char_list.append(entry)
    char_list.sort(reverse=True, key=sort_on)
    return char_list


