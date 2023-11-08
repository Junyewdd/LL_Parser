from lexical_analyzer import Lexer
from grammar import Parser
from symbol_table import SymbolTable

class Program:
    def read(content, print_type):
        symbolTable = SymbolTable()
        lexer = Lexer(content, print_type, symbolTable)
        lexer.lexical()
        parser = Parser(lexer, symbolTable)
        parser.parse()