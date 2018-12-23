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
            elif nextchar in terminator:
                break
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
            elif nextchar in terminator:
                token.append("id")
                lexeme = ''
                state = START
                break
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
            elif nextchar in terminator:
                token.append("con")
                lexeme = ''
                state = START
                break
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
            elif nextchar in terminator:
                token.append("err")
                lexeme = ''
                state = START
                break
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
            elif nextchar in terminator:
                token.append("con")
                lexeme = ''
                state = START
                break
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
    token.append("$")
    return token

def print_stack(state, popped, s):
    stack = s
    stack.reverse()
    # print("****")
    # print(state)
    # print(popped)
    # print(stack)
    print("L=>", end = " ")
    for i in popped:
        print(i, end =" ")
    for i in stack:
        print(i, end =" ")
    print()
    stack.reverse()

def parser(token):
    # print(token)
    token = terminals_checker(token)
    # print(token)
    stack = ["S"]
    popped = []
    print("L=> S")
    for inp in token:
        if inp == "id":
            while len(stack) == 0 or stack[-1] != "id":
                if len(stack) == 0:
                    print("parse error")
                    sys.exit(1)
                if stack[-1] == "S":
                    stack.pop()
                    stack.append("S")
                    stack.append(";")
                    stack.append("E")
                    stack.append("=")
                    stack.append("id")
                elif stack[-1] == "E":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                elif stack[-1] == "Ep":
                    stack.pop()
                elif stack[-1] == "T":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                elif stack[-1] == "Tp":
                    stack.pop()
                elif stack[-1] == "F":
                    stack.pop()
                    stack.append("A")
                    stack.append("id")
                elif stack[-1] == "A":
                    stack.pop()
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack("id", popped, stack)
            popped.append(stack.pop())
        elif inp == "con":
            while len(stack) == 0 or stack[-1] != "con":
                if len(stack) == 0:
                    print("parse error")
                    sys.exit(1)
                if stack[-1] == "S":
                    stack.pop()
                elif stack[-1] == "E":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                elif stack[-1] == "Ep":
                    stack.pop()
                elif stack[-1] == "T":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                elif stack[-1] == "Tp":
                    stack.pop()
                elif stack[-1] == "F":
                    stack.pop()
                    stack.append("con")
                elif stack[-1] == "A":
                    stack.pop()
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack("con", popped, stack)
            popped.append(stack.pop())
        elif inp == "+":
            while len(stack) == 0 or stack[-1] != "+":
                if len(stack) == 0:
                    print("parse error")
                    sys.exit(1)
                if stack[-1] == "S":
                    stack.pop()
                elif stack[-1] == "E":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                elif stack[-1] == "Ep":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                    stack.append("+")
                elif stack[-1] == "T":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                elif stack[-1] == "Tp":
                    stack.pop()
                elif stack[-1] == "A":
                    stack.pop()
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack("+", popped, stack)
            popped.append(stack.pop())
        elif inp == "-":
            while len(stack) == 0 or stack[-1] != "-":
                if len(stack) == 0:
                    print("parse error")
                    sys.exit(1)
                if stack[-1] == "S":
                    stack.pop()
                elif stack[-1] == "E":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                elif stack[-1] == "Ep":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                    stack.append("-")
                elif stack[-1] == "T":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                elif stack[-1] == "Tp":
                    stack.pop()
                elif stack[-1] == "A":
                    stack.pop()
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack("-", popped, stack)
            popped.append(stack.pop())
        elif inp == "*":
            while len(stack) == 0 or stack[-1] != "*":
                if len(stack) == 0:
                    print("parse error")
                    sys.exit(1)
                if stack[-1] == "S":
                    stack.pop()
                elif stack[-1] == "E":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                elif stack[-1] == "Ep":
                    stack.pop()
                elif stack[-1] == "T":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                elif stack[-1] == "Tp":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                    stack.append("*")
                elif stack[-1] == "A":
                    stack.pop()
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack("*", popped, stack)
            popped.append(stack.pop())
        elif inp == "/":
            while len(stack) == 0 or stack[-1] != "/":
                if len(stack) == 0:
                    print("parse error")
                    sys.exit(1)
                if stack[-1] == "S":
                    stack.pop()
                elif stack[-1] == "E":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                elif stack[-1] == "Ep":
                    stack.pop()
                elif stack[-1] == "T":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                elif stack[-1] == "Tp":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                    stack.append("/")
                elif stack[-1] == "A":
                    stack.pop()
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack("/", popped, stack)
            popped.append(stack.pop())
        elif inp == "(":
            while len(stack) == 0 or stack[-1] != "(":
                if len(stack) == 0:
                    print("parse error")
                    sys.exit(1)
                if stack[-1] == "S":
                    stack.pop()
                elif stack[-1] == "E":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                elif stack[-1] == "Ep":
                    stack.pop()
                elif stack[-1] == "T":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                elif stack[-1] == "Tp":
                    stack.pop()
                elif stack[-1] == "F":
                    stack.pop()
                    stack.append(")")
                    stack.append("E")
                    stack.append("(")
                elif stack[-1] == "A":
                    stack.pop()
                    stack.append(")")
                    stack.append("E")
                    stack.append("(")
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack("(", popped, stack)
            popped.append(stack.pop())
        elif inp == ")":
            while len(stack) == 0 or stack[-1] != ")":
                if len(stack) == 0:
                    print("parse error")
                    sys.exit(1)
                if stack[-1] == "S":
                    stack.pop()
                elif stack[-1] == "E":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                elif stack[-1] == "Ep":
                    stack.pop()
                elif stack[-1] == "T":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                elif stack[-1] == "Tp":
                    stack.pop()
                elif stack[-1] == "A":
                    stack.pop()
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack(")", popped, stack)
            popped.append(stack.pop())
        elif inp == ";":
            while len(stack) == 0 or stack[-1] != ";":
                if len(stack) == 0:
                    print("parse error")
                    sys.exit(1)
                if stack[-1] == "S":
                    stack.pop()
                elif stack[-1] == "E":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                elif stack[-1] == "Ep":
                    stack.pop()
                elif stack[-1] == "T":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                elif stack[-1] == "Tp":
                    stack.pop()
                elif stack[-1] == "A":
                    stack.pop()
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack(";", popped, stack)
            popped.append(stack.pop())
        elif inp == "?":
            while len(stack) == 0 or stack[-1] != "?":
                if len(stack) == 0:
                    print("parse error")
                    sys.exit(1)
                if stack[-1] == "S":
                    stack.pop()
                    stack.append("S")
                    stack.append("?")
                elif stack[-1] == "E":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                elif stack[-1] == "Ep":
                    stack.pop()
                elif stack[-1] == "T":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                elif stack[-1] == "Tp":
                    stack.pop()
                elif stack[-1] == "A":
                    stack.pop()
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack("?", popped, stack)
            popped.append(stack.pop())
        elif inp == "=":
            while len(stack) == 0 or stack[-1] != "=":
                if len(stack) == 0:
                    print("parse error")
                    sys.exit(1)
                if stack[-1] == "S":
                    stack.pop()
                elif stack[-1] == "E":
                    stack.pop()
                    stack.append("Ep")
                    stack.append("T")
                elif stack[-1] == "Ep":
                    stack.pop()
                elif stack[-1] == "T":
                    stack.pop()
                    stack.append("Tp")
                    stack.append("F")
                elif stack[-1] == "Tp":
                    stack.pop()
                elif stack[-1] == "A":
                    stack.pop()
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack("?", popped, stack)
            popped.append(stack.pop())
        elif inp == "$":
            while len(stack) != 0:
                if stack[-1] == "S":
                    stack.pop()
                elif stack[-1] == "Ep":
                    stack.pop()
                elif stack[-1] == "Tp":
                    stack.pop()
                elif stack[-1] == "A":
                    stack.pop()
                else:
                    print("parse error")
                    sys.exit(1)
                print_stack("$", popped, stack)
            # if len(stack) != 0:
            #     print("parse error")
            #     # print(stack)
            #     sys.exit(1)
        else:
            print("parse error")
            sys.exit(1)
        # print(i, end =' ')

if __name__ == '__main__':
    token = lexer()
    parser(token)    