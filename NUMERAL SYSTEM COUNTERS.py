def numerical_system_counter(start, end):
    for i in range(start, end):
        print("DEC: {}    HEX: {}    BIN: {}".format(i, hex(i)[2:].upper(), bin(i)[2:]))
    return

def main():
    loop = True
    while loop:
        print("Enter exit to end")
        start_number = input("Enter the starting number (e.g. 0) > ")
        if start_number == "exit":
            return
        else:
            pass
        end_number = input("Enter how many numbers to display (e.g. 1000) >")

        numerical_system_counter(int(start_number), int(end_number))

if __name__ == "__main__":
    main()