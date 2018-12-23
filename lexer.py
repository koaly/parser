'''
Natthapong Somboonphattarakit 5910501950
lexical analyzer in python
'''

import sys

# INIT ALPHABETS
numerics = list("0123456789")
characters = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
operators = list("+-*/()")
dot = ["."]
whitespaces = [" ", "\n", "\r", "\t"]
terminator = [""]

def lexer():
    # INIT STATES
    START = 0
    ERROR = 1
    IDEN = 2
    CONST = 3
    DOT = 4
    FRAC = 5

    # INIT START STATE
    state = START
    lexeme = ''

    # LEXICAL ANALYZER
    token = []
    while True:
        nextchar = sys.stdin.read(1)
        if state == START:
            if nextchar in numerics:
                lexeme += nextchar
                state = CONST
            elif nextchar in characters:
                lexeme += nextchar
                state = IDEN
            elif nextchar in operators:
                token.append(["LITERAL", nextchar])
            elif nextchar in whitespaces:
                continue
            elif nextchar in terminator:
                break
            else:
                token.append(["ERROR", nextchar])
        elif state == IDEN:
            if nextchar in numerics:
                lexeme += nextchar
            elif nextchar in characters:
                lexeme += nextchar
            elif nextchar in operators:
                token.append(["IDEN", lexeme])
                lexeme = ''
                token.append(["LITERAL", nextchar])
                state = START
            elif nextchar in whitespaces:
                token.append(["IDEN", lexeme])
                lexeme = ''
                state = START
            elif nextchar in terminator:
                token.append(["IDEN", lexeme])
                lexeme = ''
                state = START
                break
            else:
                token.append(["IDEN", lexeme])
                lexeme = ''
                token.append(["ERROR", nextchar])
                state = START
        elif state == CONST:
            if nextchar in numerics:
                lexeme += nextchar
            elif nextchar in characters:
                token.append(["CONST", lexeme])
                lexeme = nextchar
                state = IDEN
            elif nextchar in operators:
                token.append(["CONST", lexeme])
                lexeme = ''
                token.append(["LITERAL", nextchar])
                state = START
            elif nextchar in whitespaces:
                token.append(["CONST", lexeme])
                lexeme = ''
                state = START
            elif nextchar in dot:
                lexeme += nextchar
                state = DOT
            elif nextchar in terminator:
                token.append(["CONST", lexeme])
                lexeme = ''
                state = START
                break
            else:
                token.append(["CONST", lexeme])
                lexeme = ''
                token.append(["ERROR", nextchar])
                state = START
        elif state == DOT:
            if nextchar in numerics:
                lexeme += nextchar
                state = FRAC
            elif nextchar in characters:
                token.append(["ERROR", lexeme])
                lexeme = nextchar
                state = IDEN
            elif nextchar in operators:
                token.append(["ERROR", lexeme])
                lexeme = ''
                token.append(["LITERAL", nextchar])
                state = START
            elif nextchar in whitespaces:
                token.append(["ERROR", lexeme])
                lexeme = ''
                state = START
            elif nextchar in terminator:
                token.append(["ERROR", lexeme])
                lexeme = ''
                state = START
                break
            else:
                token.append(["ERROR", lexeme])
                lexeme = ''
                token.append(["ERROR", nextchar])
                state = START
        elif state == FRAC:
            if nextchar in numerics:
                lexeme += nextchar
            elif nextchar in characters:
                token.append(["CONST", lexeme])
                lexeme = nextchar
                state = IDEN
            elif nextchar in operators:
                token.append(["CONST", lexeme])
                lexeme = ''
                token.append(["LITERAL", nextchar])
                state = START
            elif nextchar in whitespaces:
                token.append(["CONST", lexeme])
                lexeme = ''
                state = START
            elif nextchar in terminator:
                token.append(["CONST", lexeme])
                lexeme = ''
                state = START
                break
            else:
                token.append(["CONST", lexeme])
                lexeme = ''
                token.append(["ERROR", nextchar])
                state = START
        else:
            print('Invalid token. Exiting...')
            sys.exit(1)
    return token

if __name__ == '__main__':
    token = lexer()
    for i in token:
        print("{}\t{}".format(i[0],i[1]))