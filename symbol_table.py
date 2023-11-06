
class SymbolTable:
    def __init__(self):
        self.table = {}
        
    def set(self, name, value):
        self.table[name] = value
        
    def get(self, name):
        if name in self.table:
            return self.table[name]
        else:
            raise Exception(f"{name} is not defined")
    
    def exists(self, name):
        return name in self.table