CODE ={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
            'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}

def text_to_morse(str):
    out = ""
    str = str.upper()
    for i in str:
        if i in CODE:
            out += CODE[i] + ' '
        else:
            out += i
    return out

text_in = input('Text to Morse Code Converter\nType your text message that you want to be converted into Morse Code:\n')
convert = text_to_morse(text_in)
print('Your Morse Code is:', convert)
