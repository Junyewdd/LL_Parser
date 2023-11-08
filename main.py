from lexical_analyzer import Lexer
from grammar import Parser

def main():
    text = "operand1 := 3 + (4*2);operand2 := 6"
    lexer = Lexer(text)
    lexer.lexical()
    parser = Parser(lexer)
    parser.parse()
    
if __name__ == '__main__':
    main()