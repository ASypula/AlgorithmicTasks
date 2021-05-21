import string
import matplotlib.pyplot as plt
from time import process_time
from Pattern_searching import find_KR, find_KMP, find_Naive


def get_table(path, number):
    tab = []
    i = 0
    with open(path, 'r') as fp:
        text = fp.read()
        text = text.split()
        for word in text:
            if i <= number:
                tab.append(word.strip(string.punctuation))
                i = i + 1
    return tab


def plot():
    # prepare space for data
    keys_naive = []
    values_naive = []
    keys_kmp = []
    values_kmp = []
    keys_kr = []
    values_kr = []

    # read file
    with open("pan-tadeusz.txt", 'r') as fh:
        text = fh.read()

    # main loop to measure time needed to find 100...1000 words
    for i in range(100, 1100, 100):
        # get patterns from file
        strings = get_table("pan-tadeusz.txt", i)

        # look for patterns and measure time
        start_naive = process_time()
        for j in range(i + 1):
            find_Naive(strings[j], text)
        stop_naive = process_time()
        keys_naive.append(i)
        values_naive.append(stop_naive - start_naive)

        start_kmp = process_time()
        for j in range(i + 1):
            find_KMP(strings[j], text)
        stop_kmp = process_time()
        keys_kmp.append(i)
        values_kmp.append(stop_kmp - start_kmp)

        start_kr = process_time()
        for j in range(i + 1):
            find_KR(strings[j], text, 1069)
        stop_kr = process_time()
        keys_kr.append(i)
        values_kr.append(stop_kr - start_kr)

    plt.plot(keys_naive, values_naive, label='Naive')
    plt.plot(keys_kmp, values_kmp, label='KMP')
    plt.plot(keys_kr, values_kr, label='Karp-Rabin')
    plt.title(label='Pattern searching times - alghorithms comparision')
    plt.xlabel("n")
    plt.ylabel("t [s]")
    plt.legend()
    plt.savefig('Pattern searching times.png')
    plt.show()


# if __name__ == "__main__":
plot()
