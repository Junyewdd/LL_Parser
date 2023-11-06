
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
        
    def error(self):
        raise Exception('Invalid character')
    
    def advance(self):
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
            # /
            if self.current_char == "/":
                self.advance()
                self.token_string = "/"
                self.next_token = DIV_OP
                return
            
            
            # self.error()
            
        self.token_string = ''
        self.next_token = EOF
                
        
        
        
        
        

# # 정수 변수
# next_token = None

# # 문자열 변수
# token_string = ""

# # 입력 스트림 저장하는 변수
# input_stream = ""


# # 입력 스트림을 분석하여 하나의 lexeme을 찾아낸  뒤,  그것의  token type을 next_token에 저장하고, lexeme 문자열을 token_string에 저장하는 함수

# def lexical():
#     global next_token
#     global token_string
#     global input_stream
    
#     # 입력 스트림에서 첫 번째 문자 가져옴
#     char = input_stream[0]
#     input_stream = input_stream[1:]
    
#     # lexeme이 숫자인지
#     if char.isdigit():
        
#         # 숫자 끝날 때까지 입력 스트림 순회
#         while input_stream and input_stream[0].isdigit():
#             char += input_stream[0]
#             input_stream = input_stream[1:]
            
#         next_token = INTEGER
#         token_string = char
    
#     # lexeme이 문자열인지    
#     elif char.isalpha():
#         while input_stream and input_stream[0].isalpha():
#             char += input_stream[0]
#             input_stream = input_stream[1:]
            
#         next_token = STRING
#         token_string = char
    
    
#     else:
#         # 입력 스트림이 끝났으면 EOF 반환
#         next_token = EOF
#         token_string = ""