class Printer:
    def __init__(self, print_type, symbolTable):
        self.type = print_type
        self.symbol_table = symbolTable
        
    def print_type_a(self, id, const, op, state, result):
        if self.type == 'a':
            print(f"id : {id}, const : {const}, op : {op}")
            print(state)
            if result:
                print("Result ==> ", end = " ")
                self.symbol_table.print_symbol_table()
            
    def print_type_b(self, token):
        if self.type == 'b':
            print(token)
    

    