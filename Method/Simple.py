import random
import string


def encrypt(text, keyword='', printable=False):
    alphabet = None
    cipher = None
    if printable:
        alphabet = dict.fromkeys(list(string.printable), 0)
        cipher = dict.fromkeys(list(string.printable), '')
    else:
        alphabet = dict.fromkeys(list(string.ascii_letters), 0)
        cipher = dict.fromkeys(list(string.ascii_letters), '')

    if keyword == '':
        for i in range(len(text)):
            if text[i] in alphabet.keys():
                alphabet[text[i]] += 1
    else:
        for i in range(len(keyword)):
            if keyword[i] in alphabet.keys():
                alphabet[keyword[i]] += len(keyword) - i

    alphabet = {k: v for k, v in sorted(
        alphabet.items(), key=lambda item: item[1], reverse=True)}

    for i in range(len(list(cipher.keys()))):
        key = list(cipher.keys())[i]
        cipher[key] = list(alphabet.keys())[i]

    cipher_text = ''

    for i in range(len(text)):
        if text[i] in cipher.keys():
            cipher_text += cipher[text[i]]
        else:
            cipher_text += text[i]

    return cipher, cipher_text


file = open("./test.txt", encoding="utf8")
text = file.read()

cipher, cipher_text = encrypt(text, keyword='Nima Safaei', printable=True)
print(cipher_text)
