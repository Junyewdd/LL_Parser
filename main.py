import sys


from program import Program

def main():
    with open('file1.txt', 'r') as file:
        content = file.read().strip()
    Program.read(content)
     
    # text = "operand1 := 3;operand2:= operand1* 3"
    # Program.read(text)


def process_line(line):
    Program.read(line)


if __name__ == '__main__':
    main()