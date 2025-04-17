def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)


def get_size(w, h, d):
    area = 2*(w*h + h*d + w*d)
    volume = w*h*d
    return [area, volume]



def get_min_max(seq): 
    return min(seq), max(seq)


def sp_eng(sentence): 
    return 'english' in sentence.lower()