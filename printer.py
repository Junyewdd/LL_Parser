class Printer:
    def __init__(self, print_type, symbolTable):
        self.type = print_type
        self.symbol_table = symbolTable
        
    def print_type_a(self, id, const, op, state):
        if self.type == 'a':
            print(f"id : {id}, const : {const}, op : {op}")
            print(state)
            
    def print_type_b(self, token):
        if self.type == 'b':
            print(token)
    

    