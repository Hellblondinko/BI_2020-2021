

mor = {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
       '-..': 'D',      '.': 'E',   '..-.': 'F',
       '-.': 'G',   '....': 'H',     '..': 'I',
       '.---': 'J',    '-.-': 'K',   '.-..': 'L',
       '--': 'M',     '-.': 'N',    '---': 'O',
       '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
       '...': 'S',      '-': 'T',    '..-': 'U',
       '...-': 'V',    '.--': 'W',   '-..-': 'X',
       '-.--': 'Y',   '--..': 'Z',  '-----': '0',
       '.----': '1',  '..---': '2',  '...--': '3',
       '....-': '4',  '.....': '5',  '-....': '6',
       '--...': '7',  '---..': '8',  '----.': '9'}
print('''Enter your msg in Morse.
Notic that:
    1- Use / to separate the letters and space to separate words.
    2- Your message must contain only letters and numbers.
    3- '?' in output means that your input was unknowed.
    4- Morze dictionary {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
       '-..': 'D',      '.': 'E',   '..-.': 'F',
       '-.':'G',    '....': 'H',     '..': 'I',
       '.---': 'J',    '-.-': 'K',   '.-..': 'L',
       '--': 'M',     '-.': 'N',    '---': 'O',
       '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
       '...': 'S',      '-': 'T',    '..-': 'U',
       '...-': 'V',    '.--': 'W',   '-..-': 'X',
       '-.--': 'Y',   '--..': 'Z',  '-----': '0',
       '.----': '1',  '..---': '2',  '...--': '3',
       '....-': '4',  '.....': '5',  '-....': '6',
       '--...': '7',  '---..': '8',  '----.': '9'}

    >>> ''', end='')
msg = input(' ')
out = []
letter = []
j = -1
for i in msg.split(' '):
    j += 1
    letter += [i.split('/')]
    for k in range(len(letter[j])):
        out += mor.get(letter[j][k], '?')
    out += ' '
print('\n      >>> Your msg is: ', end='')
print(''.join(out))
