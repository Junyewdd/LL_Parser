from lexical_analyzer import IDENT, CONST, ASSIGNMENT_OP, SEMI_COLON, ADD_OP, MIN_OP, MULT_OP, DIV_OP, LEFT_PAREN, RIGHT_PAREN, EOF

class Parser:
    def __init__(self, lexer, symbolTable):
        self.lexer = lexer
        self.symbol_table = symbolTable
        self.isUnknown = False
        self.current_operator = ''
        
    def error(self, message):
        print(f"Error : {message}")
        raise Exception('Invalid syntax')
        
    
    def match(self, expected_token_type):
        if self.lexer.next_token == expected_token_type or self.isUnknown == True:
            #
            self.lexer.lexical()
        else:
            print(f"Unexpected token : {self.lexer.next_token}")
            # self.error("")
    
    # <program> → <statements>
    def program(self):
        self.statements()
        self.match(EOF)
    
    # <statements> → <statement> | <statement><semi_colon><statements>
    def statements(self):
        self.statement()
        while self.lexer.next_token == SEMI_COLON:
            self.match(SEMI_COLON)
            self.statement()
            
            ##
            
    # <statement> → <ident><assignment_op><expression>
    def statement(self):
        ident_name = self.ident(True)
        self.assignment_op()
        value = self.expression()
        self.symbol_table.set(ident_name, value)
        
        
    # <expression> → <term><term_tail>
    def expression(self):
        value = self.term()
        result = self.term_tail()
        if value == "Unknown" or result == "Unknown":
            return "Unknown"
        else: 
            value += result
            return value
        
    # <term_tail> → <add_op><term><term_tail> | ε
    def term_tail(self):
        value = 0
        while self.lexer.next_token in [ADD_OP, MIN_OP]:
            isAddOp = self.add_operator()
            value = self.term()
            if value == "Unknown":
                return "Unknown"
            if isAddOp == -1:
                value *= -1
            if self.lexer.next_token == RIGHT_PAREN:
                break
            value += self.term_tail()
        return value

    # <term> → <factor> <factor_tail>
    def term(self):
        
        value = self.factor()
        
        value = self.factor_tail(value)
        return value

    # <factor_tail> → <mult_op><factor><factor_tail> | ε
    def factor_tail(self, value):
        if value == "Unknown":
            return "Unknown"
        while self.lexer.next_token in [MULT_OP, DIV_OP]:
            isMultOp = self.mult_operator()
            if isMultOp == 1:
                value *= self.factor()
            elif isMultOp == -1:
                value /= self.factor()
            value = self.factor_tail(value)
        return value

    # <factor> → <left_paren><expression><right_paren> | <ident> | <const>
    def factor(self):
        if self.lexer.next_token == LEFT_PAREN:
            self.match(LEFT_PAREN)
            value = self.expression()
            self.match(RIGHT_PAREN)
        elif self.lexer.next_token == IDENT:
            ident_name = self.ident(False)            
            if self.symbol_table.exists(ident_name):
                value = self.symbol_table.get(ident_name)
            else:
                self.isUnknown = True
                return "Unknown"
        else:
            value = self.const()
        return value
        

    # <const> → any decimal numbers
    def const(self):
        value = self.lexer.token_string
        self.match(CONST)
        try:
            return int(value)
        except ValueError:
            return float(value)

    # <ident> → any names conforming to C identifier rules
    def ident(self, isAssigned):
        ident_name = self.lexer.token_string
        # if (not isAssigned) and (not self.symbol_table.exists(ident_name)) and (not self.isUnknown):
        if (not isAssigned) and (not self.symbol_table.exists(ident_name)):
            if self.lexer.state == "(OK)":
                self.lexer.state = f"(Error) \"정의되지 않은 변수({ident_name})가 참조됨\""
            else:
                self.lexer.state += f"\n(Error) \"정의되지 않은 변수({ident_name})가 참조됨\""
            self.symbol_table.set(ident_name, "Unknown")
            self.isUnknown = True
        self.match(IDENT)
        return ident_name

    # <assignment_op> → :=
    def assignment_op(self):
        self.match(ASSIGNMENT_OP)

    # <semi_colon> → ;
    def semi_colon(self):
        self.match(SEMI_COLON)

    # <add_operator> → + | -
    def add_operator(self):
        if self.lexer.next_token == ADD_OP:
            self.match(ADD_OP)
            self.check_consecutive_operators(ADD_OP)
            
            return 1
        elif self.lexer.next_token == MIN_OP:
            self.match(MIN_OP)
            self.check_consecutive_operators(MIN_OP)
            return -1
        else:
            self.error("Expected a multiplication or division operator")

    # <mult_operator> → * | /
    def mult_operator(self):
        if self.lexer.next_token == MULT_OP:
            self.match(MULT_OP)
            self.check_consecutive_operators(MULT_OP)
            return 1
        elif self.lexer.next_token == DIV_OP:
            self.match(DIV_OP)
            self.check_consecutive_operators(DIV_OP)
            return -1
        else:
            self.error("Expected a multiplication or division operator")

    # <left_paren> → (
    def left_paren(self):
        self.match(LEFT_PAREN)
        
    # <right_paren> → )
    def right_paren(self):
        self.match(RIGHT_PAREN)
        
    def parse(self):
        self.program()
        self.match(EOF)
        if self.lexer.print_type == 'a':
            print("Result ==> ", end = " ")
            self.symbol_table.print_symbol_table()
    
    def setState(self, sentence):
        if self.lexer.state == "(OK)":
            self.lexer.state = sentence
        else:
            self.lexer.state += sentence
    
    def check_consecutive_operators(self, token_type):
        TOKEN_DICT={ADD_OP:"+", MIN_OP:"-", MULT_OP:"*", DIV_OP:"/"}
        check = False
        while self.lexer.next_token == token_type:
            self.lexer.skip_print = True
            self.match(token_type)
            if check == False:
                self.setState(f"(Warning) 중복 연산자({TOKEN_DICT[token_type]}) 제거")
                check = True
        self.lexer.skip_print = False
        if self.lexer.token_string == '':
            self.lexer.lexical()
        
            