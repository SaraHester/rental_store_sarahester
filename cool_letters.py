def print_cool_letters(letters):
    blocks = map(find_cool_letters, letters)
    print('\n'.join(map('\t'.join, zip(*blocks))))
def find_cool_letters(letter):
    #CAPITAL LETTERS
    if letter == 'A':
        return ['░█▀▀█', 
                '▒█▄▄█',
                '▒█░▒█']
    elif letter == 'B':
        return ['▒█▀▀█', 
                '▒█▀▀▄', 
                '▒█▄▄█']
    elif letter == 'C':
        return['█▀▀', 
               '█░░ ',
                '▀▀▀' ]
    elif letter == 'D':
        return ['▒█▀▀▄', 
                '▒█░▒█ ',
                '▒█▄▄▀ ']
    elif letter == 'E':
        return ['▒█▀▀▀',
                '▒█▀▀▀',
                '▒█▄▄▄']
    elif letter == 'F':
        return ['▒█▀▀▀',
                '▒█▀▀▀', 
                '▒█░░░']
    elif letter == 'G':
        return ['▒█▀▀█', 
                '▒█░▄▄', 
                '▒█▄▄█ ']
    elif letter == 'H':
        return ['▒█░▒█',
                '▒█▀▀█', 
                '▒█░▒█']
    elif letter == "I":
        return ['▀█▀', 
                '▒█░', 
                '▄█▄']
    elif letter == 'J':
        return ['░░░▒█',
                '░▄░▒█', 
                '▒█▄▄█']
    elif letter == 'K':
        return ['▒█░▄▀',
                '▒█▀▄░', 
                '▒█░▒█']
    elif letter == 'L':
        return ['▒█░░░', 
                '▒█░░░', 
                '▒█▄▄░']
    elif letter == 'M':
        return ['▒█▀▄▀█', 
                '▒█▒█▒█', 
                '▒█░░▒█']
    elif letter == 'N':
        return ['▒█▄░▒█',
                '▒█▒█▒█',
                '▒█░░▀█']
    elif letter == 'O':
        return['▒█▀▀▀█',
                '▒█░░▒█', 
                '▒█▄▄▄█']
    elif letter == 'P':
        return ['▒█▀▀█',
                '▒█▄▄█',
                '▒█░░░ ']
    elif letter == 'Q':
        return ['▒█▀▀█', 
                '▒█░▒█', 
                '░▀▀█▄']
    elif letter == 'R':
        return['▒█▀▀█',
                '▒█▄▄▀', 
                '▒█░▒█ ']
    elif letter == 'S':
        return ['▒█▀▀▀█',
                '░▀▀▀▄▄', 
                '▒█▄▄▄█ ']
    elif letter == 'T':
        return ['▀▀█▀▀',
                '░▒█░░', 
                '░▒█░░']
    elif letter == 'U':
        return ['▒█░▒█',
                '▒█░▒█',
                '░▀▄▄▀ ']
    elif letter == 'V':
        return ['▒█░░▒█', 
                '░▒█▒█░', 
                '░░▀▄▀░']
    elif letter == 'W':
        return ['▒█░░▒█', 
                '▒█▒█▒█', 
                '▒█▄▀▄█']
    elif letter == 'X':
        return ['▀▄▒▄▀', 
                '░▒█░░', 
                '▄▀▒▀▄']
    elif letter == 'Y':
        return ['▒█░░▒█', 
                '▒█▄▄▄█', 
                '░░▒█░░']
    elif letter == 'Z':
        return ['▒█▀▀▀█', 
                '░▄▄▄▀▀', 
                '▒█▄▄▄█']
    elif letter == ' ':
        return ['   ',
                '   ',
                '   ']
    # lowercase
    elif letter == 'a':
        return ['█▀▀█', 
                '█▄▄█',
                '▀░░▀']
    elif letter == 'b':
        return ['█▀▀▄', 
                '█▀▀▄', 
                '▀▀▀░']
    elif letter == 'c':
        return ['█▀▀', 
                '█░░', 
                '▀▀▀'] 
    elif letter == 'd':
        return ['█▀▀▄', 
                '█░░█', 
                '▀▀▀░']
    elif letter == 'e':
        return ['█▀▀', 
                '█▀▀', 
                '▀▀▀']
    elif letter == 'f':
        return ['█▀▀', 
                '█▀▀', 
                '▀░░']
    elif letter == 'g':
        return ['█▀▀▀',
                '█░▀█', 
                '▀▀▀▀']
    elif letter == 'h':
        return ['█░░█',
                '█▀▀█', 
                '▀░░▀']
    elif letter == 'i':
        return ['░▀░', 
                '▀█▀', 
                '▀▀▀']
    elif letter == 'j':
        return ['░░▀', 
                '░░█', 
                '█▄█']
    elif letter == 'k':
        return ['█░█', 
                '█▀▄', 
                '▀░▀']
    elif letter == 'l':
        return ['█░░', 
                '█░░', 
                '▀▀▀']
    elif letter == 'm':
        return ['█▀▄▀█', 
                '█░▀░█', 
                '▀░░░▀']
    elif letter == 'n':
        return ['█▀▀▄', 
                '█░░█', 
                '▀░░▀']
    elif letter == 'o':
        return ['█▀▀█', 
                '█░░█', 
                '▀▀▀▀']
    elif letter == 'p':
        return ['█▀▀█', 
                '█░░█', 
                '█▀▀']
    elif letter == 'q':
        return ['█▀▀█', 
                '█░░█', 
                '▀▀▀█']
    elif letter == 'r':
        return ['█▀▀█', 
                '█▄▄▀', 
                '▀░▀▀']
    elif letter == 's':
        return ['█▀▀',
                '▀▀█', 
                '▀▀▀']
    elif letter == 't':
        return ['▀▀█▀▀', 
                '░░█░░', 
                '░░▀░░']
    elif letter == 'u':
        return ['█░░█', 
                '█░░█', 
                '░▀▀▀']
    elif letter == 'v':
        return ['▀█░█▀', 
               '░█▄█░', 
                '░░▀░']
    elif letter == 'w':
        return ['█░░░█', 
                '█▄█▄█', 
                '░▀░▀░']
    elif letter == 'x':
        return ['█░█', 
                '▄▀▄', 
                '▀░▀']
    elif letter == 'y':
        return ['█░░█', 
                '█▄▄█', 
                '▄▄▄█']
    elif letter == 'z':
        return ['▀▀█', 
                '▄▀░', 
                '▀▀▀']
    elif letter == '.':
        return ['░', 
                '▄', 
                '█']
    elif letter == '!':
        return ['█', 
                '▀', 
                '▄']
    elif letter == '-':
        return ['  ',
                '▀▀',
                '  ']