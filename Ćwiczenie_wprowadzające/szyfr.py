import sys
import argparse

def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE')
    args = parser.parse_args(arguments[1:])
    path = args.FILE

    print(f"Nazwa pliku to: {path}") # testowy print

    with open(path, 'r') as file_handle:
        text = file_handle.read()
        text = text.split(" ")
        for line in text:
            print(line)
        print(text[0])
        print(text[1:2])  # wiecej testowych printow



if __name__ == "__main__":
    main(sys.argv)
