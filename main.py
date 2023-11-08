import sys


from program import Program

def main():
    
    print_type = 'b'
    
    with open('file1.txt', 'r') as file:
        content = file.read().strip()
        
    Program.read(content, print_type)
     
    # text = "operand1 := 3;operand2:= operand1* 3"
    # Program.read(text)


def process_line(line):
    Program.read(line)


if __name__ == '__main__':
    main()