def get_word_count(text):
    return len(text.split())

def letter_count(text):
    letter_dict = {}
    text = text.lower()
    for i in text:
        
        if i not in letter_dict:
            letter_dict.setdefault(i, 1)
        elif i in letter_dict:
            letter_dict[i] += 1
    sorted_dict = dict(sorted(letter_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict