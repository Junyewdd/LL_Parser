from lexical_analyzer import IDENT, CONST, ASSIGNMENT_OP, SEMI_COLON, ADD_OP, MIN_OP, MULT_OP, DIV_OP, LEFT_PAREN, RIGHT_PAREN, EOF

from symbol_table import SymbolTable

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.symbol.table = SymbolTable
        
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
        
    # <expression> → <term><term_tail>
    def expression(self):
        print("expression")
        self.term()
        self.term_tail()
        
    # <term_tail> → <add_op><term><term_tail> | ε
    def term_tail(self):
        print("term_tail")
        if self.lexer.next_token == ADD_OP:
            self.add_operator()
            self.term()
            self.term_tail()

    # <term> → <factor> <factor_tail>
    def term(self):
        print("term")
        self.factor()
        self.factor_tail()

    # <factor_tail> → <mult_op><factor><factor_tail> | ε
    def factor_tail(self):
        print("factor_tail")
        if self.lexer.next_token == MULT_OP:
            self.mult_operator()
            self.factor()
            self.factor_tail()

    # <factor> → <left_paren><expression><right_paren> | <ident> | <const>
    def factor(self):
        print("factor")
        if self.lexer.next_token == LEFT_PAREN:
            self.match(LEFT_PAREN)
            self.expression()
            self.match(RIGHT_PAREN)
        elif self.lexer.next_token == IDENT:
            self.ident()
        else:
            self.const()
        

    # <const> → any decimal numbers
    def const(self):
        print("const")
        self.match(CONST)

    # <ident> → any names conforming to C identifier rules
    def ident(self):
        print("ident")
        self.match(IDENT)

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
        elif self.lexer.next_token == MIN_OP:
            self.match(MIN_OP)
        else:
            self.error("Expected a multiplication or division operator")

    # <mult_operator> → * | /
    def mult_operator(self):
        print("mult_operator")
        if self.lexer.next_token == MULT_OP:
            self.match(MULT_OP)
        elif self.lexer.next_token == DIV_OP:
            self.match(DIV_OP)
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




        

   
    
    



# #####

# # <program> → <statements>
# def program():
#     statements()
    
# # <statements> → <statement> | <statement><semi_colon><statements>
# def statements():
#     statement()
#     if next_token == SEMI_COLON:
#         match(SEMI_COLON)

# # <statement> → <ident><assignment_op><expression>
# def statement():
#     ident()
#     assignment_op()
#     expression()

# # <expression> → <term><term_tail>
# def expression():
#     term()
#     term_tail()

# # <term_tail> → <add_op><term><term_tail> | ε
# def term_tail():
#     if next_token == ADD_OP:
#         add_operator()
#         term()
#         term_tail()

# # <term> → <factor> <factor_tail>
# def term():
#     factor()
#     factor_tail()

# # <factor_tail> → <mult_op><factor><factor_tail> | ε
# def factor_tail():
#     if next_token == MULT_OP:
#         mult_operator()
#         factor()
#         factor_tail()

# # <factor> → <left_paren><expression><right_paren> | <ident> | <const>
# def factor():
#     if next_token == LEFT_PAREN:
#         match(LEFT_PAREN)
#         expression()
#         match(RIGHT_PAREN)
#     elif next_token == IDENT:
#         ident()
#     else:
#         const()

# # <const> → any decimal numbers
# def const():
#     match(CONST)

# # <ident> → any names conforming to C identifier rules
# def ident():
#     match(IDENT)

# # <assignment_op> → :=
# def assignment_op():
#     match(ASSIGNMENT_OP)

# # <semi_colon> → ;
# def semi_colon():
#     match(SEMI_COLON)

# # <add_operator> → + | -
# def add_operator():
#     if next_token == ADD_OP:
#         match(ADD_OP)
#     elif next_token == MIN_OP:
#         match(MIN_OP)
#     else:
#         error("Expected a multiplication or division operator")

# # <mult_operator> → * | /
# def mult_operator():
#     if next_token == MULT_OP:
#         match(MULT_OP)
#     elif next_token == DIV_OP:
#         match(DIV_OP)
#     else:
#         error("Expected a multiplication or division operator")

# # <left_paren> → (
# def left_paren():
#     match(LEFT_PAREN)
    
# # <right_paren> → )
# def right_paren():
#     match(RIGHT_PAREN)



# def match(expected_token):
#     global next_token
    
#     # 현재 토큰이 expected_token과 일치하는지 확인
#     if next_token == expected_token:
#         lexical_analyzer.lexical()
#     else:
#         print(f"Unexpected token : {next_token}")
    

# def error(message):
#     print(f"Error : {message}")
#     sys.exit(1)