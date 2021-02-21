def print_board():
    size = int(input("Enter size: "))
    x = 1
    while x <= size:
        print(" ---" * size + "\n" + "| " * (size+1))
        x = x + 1
        print(" ---" * size)
        if __name__ == "__main__":
            print_board()
            input()

print_board()
