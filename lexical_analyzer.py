
# # 토큰 타입을 상수로 정의
# INTEGER, STRING, EOF = 0, 1, None

IDENT = "IDENT"
CONST = "CONST"
ASSIGNMENT_OP = "ASSIGNMENT_OP"
SEMI_COLON = "SEMI_COLON"
ADD_OP = "ADD_OP"
MIN_OP = "MIN_OP"
MULT_OP = "MULT_OP"
DIV_OP = "DIV_OP"
LEFT_PAREN = "LEFT_PAREN"
RIGHT_PAREN = "RIGHT_PAREN"
EOF = "EOF"


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
class Lexer:
    def __init__(self, text):
        self.text = text
        self.current_char = self.text[0]
        self.pos = 0
        next_token = None
        token_string = ''
        self.sentence=''
        
    def split_statements(self,content):
        return content.split(';')
        
    def error(self):
        raise Exception('Invalid character')
    
    def advance(self):
        self.sentence += self.text[self.pos]
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
            
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
            
    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def word(self):
        result = ''
        while self.current_char is not None and self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == '_':
            result += self.current_char
            self.advance()
        return result
    
    ###
    def lexical(self):
        while self.current_char is not None:
            # 공백
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            # 식별자
            if self.current_char.isalpha():
                self.token_string = self.word()
                self.next_token = IDENT
                return
            # 숫자
            if self.current_char.isdigit():
                self.token_string = str(self.integer())
                self.next_token = CONST
                return
            # :=    
            if self.current_char == ":":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    self.token_string = ":="
                    self.next_token = ASSIGNMENT_OP
                    return
            # ;
            if self.current_char == ";":
                self.advance()
                self.token_string = ";"
                self.next_token = SEMI_COLON
                print(self.sentence)
                self.sentence = ''
                return
            # +
            if self.current_char == "+":
                self.advance()
                self.token_string = "+"
                self.next_token = ADD_OP
                return
            # -
            if self.current_char == "-":
                self.advance()
                self.token_string = "-"
                self.next_token = MIN_OP
                return
            # *
            if self.current_char == "*":
                self.advance()
                self.token_string = "*"
                self.next_token = MULT_OP
                return
            # /
            if self.current_char == "/":
                self.advance()
                self.token_string = "/"
                self.next_token = DIV_OP
                return
            # (
            if self.current_char == "(":
                self.advance()
                self.token_string = "("
                self.next_token = LEFT_PAREN
                return
            # /
            if self.current_char == ")":
                self.advance()
                self.token_string = ")"
                self.next_token = RIGHT_PAREN
                return
        
            # self.error()
            
        if self.sentence:
            print(self.sentence)
            self.sentence = None
        
        self.token_string = ''
        self.next_token = EOF