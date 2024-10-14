letter_to_symbol = {
    'a': '!', 'b': '@', 'c': '#', 'd': '$', 'e': '%',
    'f': '^', 'g': '&', 'h': '*', 'i': '(', 'j': ')',
    'k': '-', 'l': '=', 'm': '+', 'n': '{', 'o': '}',
    'p': '[', 'q': ']', 'r': ';', 's': ':', 't': '"',
    'u': '<', 'v': '>', 'w': '?', 'x': '/', 'y': '~', 'z': '`',
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
    'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '0',
    'K': 'a', 'L': 'b', 'M': 'c', 'N': 'd', 'O': 'e',
    'P': 'f', 'Q': 'g', 'R': 'h', 'S': 'i', 'T': 'j',
    'U': 'k', 'V': 'l', 'W': 'm', 'X': 'n', 'Y': 'o', 'Z': 'p'
}

symbol_to_letter = {value: key for key, value in letter_to_symbol.items()}

infile = open('encrypted.txt','r')

file_text = infile.read()


encrypted_text = ""
decrypted_text = ""

# for code in file_text:
#     encrypted_text += code

for code in file_text:
    if code in symbol_to_letter:
       decrypted_text += symbol_to_letter[code]
    else:
        decrypted_text += code

print(decrypted_text)

infile.close()


    