import sys
import argparse


def main(arguments):
    # parser = argparse.ArgumentParser()
    # parser.add_argument('FILE')
    # args = parser.parse_args(arguments[1:])
    # path = args.FILE

    path = "pan-tadeusz.txt"

    huge_list = []

    with open(path, "r") as f:
        huge_list = f.read().split()
    pass

if __name__ == "__main__":
    main(sys.argv)
