import sys
from program import Program

def main():
    
    print_type = 'a'
    
    if len(sys.argv) > 2 and sys.argv[1] =='-v':
        print_type = 'b'
    
    if len(sys.argv) > 1:
        file_path = sys.argv[-1]
    
    with open(file_path, 'r') as file:
        content = file.read().strip()
        
    Program.read(content, print_type)


if __name__ == '__main__':
    main()