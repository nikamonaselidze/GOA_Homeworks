def array(string):
  res = ' '.join(string.split(',')[1:-1])
  return res if len(res) > 0 else None



def temple_strings(obj, feature): 
    return obj+" are " + feature


def contamination(text, char):
  return char*len(text)


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


def obfuscate(email):
    return email.replace("@", " [at] ").replace(".", " [dot] ")