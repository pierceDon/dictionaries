file_object = open('sometext.txt', 'r')
lines = file_object.readlines()
file_content = []
word_frequency = {}

def cleanText(arg):
    arg = arg.lower()
    if "," in arg:
        arg = arg.replace(',','')
    elif "." in arg:
        arg = arg.replace('.','')
    return arg

# for line in lines:
#      split_lines = line.split()
#      for x in split_lines:
#           file_content.append(x)

for line in lines:
    line = cleanText(line)
    file_content.extend(line.split())

for x in file_content:
    word_frequency[x] = file_content.count(x)

print(word_frequency)



