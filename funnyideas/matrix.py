import os
import sys
import msvcrt  # Windows-specific library for keypress detection

def create_matrix(rows, cols, default_value=" "):
    return [[default_value for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    for row in matrix:
        print(''.join(str(cell) for cell in row))

def create_map(matrix, train_pos):
    # First row
    farm_text = "Farm ----"
    oil_text = "Oil ----"
    yard_text = "Yard ---------------------"

    # Add Farm
    start_farm = 3
    for i, char in enumerate(farm_text):
        matrix[0][start_farm + i] = char

    # Add Oil
    start_oil = 18
    for i, char in enumerate(oil_text):
        matrix[0][start_oil + i] = char

    # Add Yard
    start_yard = 54
    for i, char in enumerate(yard_text):
        matrix[0][start_yard + i] = char

    # Second row (dashes, numbers and slashes)
    dashes = "------------\\1------------\\2--------------------/3--------/4--------------------\\5----"
    for i, char in enumerate(dashes):
        matrix[1][i] = char

    # Third row (Saw Mill)
    saw_mill = "                                   Saw Mill ----"
    for i, char in enumerate(saw_mill):
        matrix[2][i] = char

    # Add train
    matrix[1][train_pos] = "T"

def get_key():
    # Using msvcrt to get keypresses on Windows
    ch = msvcrt.getch()

    # Check for special keys (escape sequence for arrow keys)
    if ch == b'\x1b':  # Escape character, which precedes arrow keys
        ch2 = msvcrt.getch()  # Get [
        ch3 = msvcrt.getch()  # Get the arrow key
        if ch3 == b'D':  # a
            return 'a'
        elif ch3 == b'C':  # d
            return 'd'
        else:
            return None  # Handle other special keys if needed
    else:
        return ch.decode('utf-8')  # Decode regular characters

def main():
    train_pos = 0
    while True:
        os.system('cls')  # Clear screen for Windows
        matrix = create_matrix(3, 86)
        create_map(matrix, train_pos)
        print_matrix(matrix)
        print("\nUse left/right arrow keys to move train (q to quit)")

        key = get_key()

        if key == 'q':  # Quit
            break

        if key == 'a' and train_pos > 0:  # a
            train_pos -= 1
        elif key == 'd' and train_pos < 85:  # d
            train_pos += 1

        if key == '1':
            print("hi")
            matrix[2][13] = "-"

# Run the main function
if __name__ == "__main__":
    main()
