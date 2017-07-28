def line(n):
    line_str = ''
    for i in range(n):
        line_str = line_str + '#'

    return line_str

def square(n):
    square_str = ''
    for i in range(n):
        square_str += (line(n)+'\n')
    return square_str

def main():
    print(square(5))

if __name__ == "__main__":
    main()
