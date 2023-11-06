from lexical_analyzer import IDENT, CONST, ASSIGNMENT_OP, SEMI_COLON, ADD_OP, MIN_OP, MULT_OP, DIV_OP, LEFT_PAREN, RIGHT_PAREN, EOF

from symbol_table import SymbolTable

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.symbol_table = SymbolTable()
        
    def error(self, message):
        print(f"Error : {message}")
        raise Exception('Invalid syntax')
        
    
    def match(self, expected_token_type):
        if self.lexer.next_token == expected_token_type:
            self.lexer.lexical()
        else:
            print(f"Unexpected token : {self.lexer.next_token}")
            self.error("")
    
    # <program> → <statements>
    def program(self):
        print("program")
        self.statements()
        self.match(EOF)
    
    # <statements> → <statement> | <statement><semi_colon><statements>
    def statements(self):
        print("statements")
        self.statement()
        while self.lexer.next_token == SEMI_COLON:
            self.match(SEMI_COLON)
            self.statement()
            
    # <statement> → <ident><assignment_op><expression>
    def statement(self):
        print("statement")
        ident_name = self.ident()
        self.assignment_op()
        value = self.expression()
        self.symbol_table.set(ident_name, value)
        print(ident_name)
        print(self.symbol_table.get(ident_name))
        
    # <expression> → <term><term_tail>
    def expression(self):
        print("expression")
        value = self.term()
        value += self.term_tail()
        return value
        
    # <term_tail> → <add_op><term><term_tail> | ε
    def term_tail(self):
        print("term_tail")
        value = 0
        if self.lexer.next_token == ADD_OP:
            isAddOp = self.add_operator()
            value = self.term()
            if(isAddOp == 1):
                value += self.term_tail()
            elif(isAddOp == -1):
                value -= self.term_tail()            
        return value

    # <term> → <factor> <factor_tail>
    def term(self):
        print("term")
        value = self.factor()
        value *= self.factor_tail()
        return value

    # <factor_tail> → <mult_op><factor><factor_tail> | ε
    def factor_tail(self):
        print("factor_tail")
        if self.lexer.next_token == MULT_OP:
            isMultOp = self.mult_operator()
            value = self.factor()
            if isMultOp == 1:
                value *= self.factor_tail()
            elif isMultOp == -1:
                value /= self.factor_tail()
        else: 
            value = 1
        return value

    # <factor> → <left_paren><expression><right_paren> | <ident> | <const>
    def factor(self):
        print("factor")
        if self.lexer.next_token == LEFT_PAREN:
            self.match(LEFT_PAREN)
            value = self.expression()
            self.match(RIGHT_PAREN)
        elif self.lexer.next_token == IDENT:            
            value = self.ident()
        else:
            value = self.const()
        return value
        

    # <const> → any decimal numbers
    def const(self):
        print("const")
        value = self.lexer.token_string
        self.match(CONST)
        try:
            return int(value)
        except ValueError:
            return float(value)

    # <ident> → any names conforming to C identifier rules
    def ident(self):
        print("ident")
        ident_name = self.lexer.token_string
        self.match(IDENT)
        return ident_name

    # <assignment_op> → :=
    def assignment_op(self):
        print("assignment_op")
        self.match(ASSIGNMENT_OP)

    # <semi_colon> → ;
    def semi_colon(self):
        print("semi_colon")
        self.match(SEMI_COLON)

    # <add_operator> → + | -
    def add_operator(self):
        print("add_operator")
        if self.lexer.next_token == ADD_OP:
            self.match(ADD_OP)
            return 1
        elif self.lexer.next_token == MIN_OP:
            self.match(MIN_OP)
            return -1
        else:
            self.error("Expected a multiplication or division operator")

    # <mult_operator> → * | /
    def mult_operator(self):
        print("mult_operator")
        if self.lexer.next_token == MULT_OP:
            self.match(MULT_OP)
            return 1
        elif self.lexer.next_token == DIV_OP:
            self.match(DIV_OP)
            return -1
        else:
            self.error("Expected a multiplication or division operator")

    # <left_paren> → (
    def left_paren(self):
        print("left_paren")
        self.match(LEFT_PAREN)
        
    # <right_paren> → )
    def right_paren(self):
        print("right_paren")
        self.match(RIGHT_PAREN)
        
    def parse(self):
        print("parse")
        self.program()
        self.match(EOF)