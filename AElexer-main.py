# token definitions
EOF = 0
ERROR = 1
LITERAL = 2
IDEN = 3
CONST = 4

# ---- main ---- #
infile = sys.stdin
lexer.state = START   # lexer's state, initialized to the start state
lexer.char = ''       # latest input character
while True:
    token, lexeme = lexer(infile)
    if token == EOF:
        break
    if token == IDEN:
        print('IDEN', end='\t')
    elif token == CONST:
        print('CONST', end='\t')
    elif token == LITERAL:
        print('LITERAL', end='\t')
    elif token == ERROR:
        print('ERROR', end='\t')
    else:
        print('Invalid token. Exiting...')
        sys.exit(1)
    print(lexeme)
