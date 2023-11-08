from lexical_analyzer import Lexer
from grammar import Parser

class Program:
    def read(content):
        lexer = Lexer(content)
        lexer.lexical()
        parser = Parser(lexer)
        parser.parse()