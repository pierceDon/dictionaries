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

infile = open('info_security.txt','r')
outfile = open('encrypted.txt','w')

infile_text = infile.read()

encrypted_text = ""


for letter in infile_text:
    if letter in letter_to_symbol:
        encrypted_text += letter_to_symbol[letter]
    else:
        encrypted_text += letter

#print(encrypted_text)

outfile.write(encrypted_text)


infile.close()
outfile.close()
    