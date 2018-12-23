'''
Natthapong Somboonphattarakit 5910501950
ll(1) parser in python
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
        if nextchar in terminator:
            break
        if state == START:
            if nextchar in numerics:
                lexeme += nextchar
                state = CONST
            elif nextchar in characters:
                lexeme += nextchar
                state = IDEN
            elif nextchar in operators:
                token.append(nextchar)
            elif nextchar in whitespaces:
                continue
            else:
                token.append(nextchar)
        elif state == IDEN:
            if nextchar in numerics:
                lexeme += nextchar
            elif nextchar in characters:
                lexeme += nextchar
            elif nextchar in operators:
                token.append("id")
                lexeme = ''
                token.append(nextchar)
                state = START
            elif nextchar in whitespaces:
                token.append("id")
                lexeme = ''
                state = START
            else:
                token.append("id")
                lexeme = ''
                token.append(nextchar)
                state = START
        elif state == CONST:
            if nextchar in numerics:
                lexeme += nextchar
            elif nextchar in characters:
                token.append("con")
                lexeme = nextchar
                state = IDEN
            elif nextchar in operators:
                token.append("con")
                lexeme = ''
                token.append(nextchar)
                state = START
            elif nextchar in whitespaces:
                token.append("con")
                lexeme = ''
                state = START
            elif nextchar in dot:
                lexeme += nextchar
                state = DOT
            else:
                token.append("con")
                lexeme = ''
                token.append(nextchar)
                state = START
        elif state == DOT:
            if nextchar in numerics:
                lexeme += nextchar
                state = FRAC
            elif nextchar in characters:
                token.append("err")
                lexeme = nextchar
                state = IDEN
            elif nextchar in operators:
                token.append("err")
                lexeme = ''
                token.append(nextchar)
                state = START
            elif nextchar in whitespaces:
                token.append("err")
                lexeme = ''
                state = START
            else:
                token.append("err")
                lexeme = ''
                token.append(nextchar)
                state = START
        elif state == FRAC:
            if nextchar in numerics:
                lexeme += nextchar
            elif nextchar in characters:
                token.append("con")
                lexeme = nextchar
                state = IDEN
            elif nextchar in operators:
                token.append("con")
                lexeme = ''
                token.append(nextchar)
                state = START
            elif nextchar in whitespaces:
                token.append("con")
                lexeme = ''
                state = START
            else:
                token.append("con")
                lexeme = ''
                token.append(nextchar)
                state = START
        else:
            print('Invalid token. Exiting...')
            sys.exit(1)
    return token

def terminals_checker(token):
    for i in range(len(token)):
        if token[i] not in ["id", "con", "+", "-", "*", "/", "(", ")", "?", ";", "="]:
            token[i] = "err"
    return token

def parser(token):
    token = terminals_checker(token)
    for i in token:
        print(i, end =' ')

if __name__ == '__main__':
    token = lexer()
    parser(token)    