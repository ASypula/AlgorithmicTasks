import sys
import argparse


def character_choice(c):
    if c >= 65 and c <= 90:
        return c
    elif c >= 97 and c <= 122:
        return c - 32
    else:
        return None


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE')
    args = parser.parse_args(arguments[1:])
    path = args.FILE

    morse_letters = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--..", ".-.-.-", ".----",
    "..---", "...--", "....-", ".....", "-....", "--...", "---..",
    "----.", "-----"
    ]

    with open(path, 'r') as file_handle:
        text = file_handle.read()
        count = 0
        for line in text:
            for c in line:
                if c == " ":
                    count = count + 1
                    if count == 1:
                        print("/ ", end='')
                    else:
                        continue
                else:
                    letter_num = character_choice(ord(c))
                    if letter_num is not None:
                        count = 0
                        print(morse_letters[letter_num - 65] + " ", end='')
                    else:
                        count = count + 1
            if c == "\n":
                print('')


if __name__ == "__main__":
    main(sys.argv)
