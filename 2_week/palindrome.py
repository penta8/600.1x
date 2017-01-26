import string


def palyndrome(text):
    if text.lower() != text:
        text = text.lower()

    newText = ''
    for index in range(len(text)):
        if text[index] in string.ascii_lowercase:
            newText += text[index]

    if newText == '' or len(newText) == 1:
        return True
    else:
        return newText[0] == newText[-1] and palyndrome(newText[1:-1])

napoleon = 'Able was I, ere I saw Elba'
michaels = 'Are we not drawn onward, we few, drawn onward to new era?'

print(palyndrome(napoleon))
print(palyndrome(michaels))
print(palyndrome('locaacol'))
print(palyndrome('arampmara'))
print(palyndrome('loco'))
