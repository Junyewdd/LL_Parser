from program import Program

def main():
    
    print_type = 'a'
    
    with open('file1.txt', 'r') as file:
        content = file.read().strip()
        
    Program.read(content, print_type)


if __name__ == '__main__':
    main()