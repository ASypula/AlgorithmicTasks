import random
from Pattern_searching import find_Naive, find_KMP, find_KR


def test_empty_text_Naive():
    text = ""
    string = "Love algorithms"
    result = find_Naive(string, text)
    assert(result == [])


def test_empty_text_KMP():
    text = ""
    string = "Love algorithms"
    result = find_KMP(string, text)
    assert(result == [])


def test_empty_text_KR():
    text = ""
    string = "Love algorithms"
    result = find_KR(string, text, 11)
    assert(result == [])


def test_empty_both_Naive():
    text = ""
    string = ""
    result = find_Naive(string, text)
    assert(result == [])


def test_empty_both_KMP():
    text = ""
    string = ""
    result = find_KMP(string, text)
    assert(result == [])


def test_empty_both_KR():
    text = ""
    string = ""
    result = find_KR(string, text, 11)
    assert(result == [])


def test_both_equal_Naive():
    text = "Love algorithms"
    string = "Love algorithms"
    result = find_Naive(string, text)
    assert(result == [0])


def test_both_equal_KMP():
    text = "Love algorithms"
    string = "Love algorithms"
    result = find_KMP(string, text)
    assert(result == [0])


def test_both_equal_KR():
    text = "Love algorithms"
    string = "Love algorithms"
    result = find_KR(string, text, 23)
    assert(result == [0])


def test_string_longer_Naive():
    text = "Love"
    string = "Love algorithms"
    result = find_Naive(string, text)
    assert(result == [])


def test_string_longer_KMP():
    text = "Love"
    string = "Love algorithms"
    result = find_KMP(string, text)
    assert(result == [])


def test_string_longer_KR():
    text = "Love"
    string = "Love algorithms"
    result = find_KR(string, text, 23)
    assert(result == [])


def test_no_pattern_Naive():
    text = "To be continued"
    string = "Love algorithms"
    result = find_Naive(string, text)
    assert(result == [])


def test_no_pattern_KMP():
    text = "To be continued"
    string = "Love algorithms"
    result = find_KMP(string, text)
    assert(result == [])


def test_no_pattern_KR():
    text = "To be continued"
    string = "Love algorithms"
    result = find_KR(string, text, 23)
    assert(result == [])


def test_Naive_1():
    text = "ABBBAABBAB"
    string = "AB"
    result = find_Naive(string, text)
    assert(result == [0, 5, 8])


def test_Naive_2():
    text = "BBBAABBAB"
    string = "AB"
    result = find_Naive(string, text)
    assert(result == [4, 7])


def test_Naive_3():
    text = "BABAABBAB"
    string = "AB"
    result = find_Naive(string, text)
    assert(result == [1, 4, 7])


def test_all_random1():
    text = []
    string = []
    for i in range(12):
        text += random.choice(["A", "B"])
    for i in range(3):
        string += random.choice(["A", "B"])
    result1 = find_Naive(string, text)
    result2 = find_KMP(string, text)
    result3 = find_KR(string, text, 23)

    assert(result1 == result2)
    assert(result2 == result3)


def test_all_random2():
    text = []
    string = []
    for i in range(25):
        text += random.choice(["A", "B"])
    for i in range(3):
        string += random.choice(["A", "B"])
    result1 = find_Naive(string, text)
    result2 = find_KMP(string, text)
    result3 = find_KR(string, text, 23)
    assert(result1 == result2 == result3)


def test_all_random3():
    text = []
    string = []
    for i in range(34):
        text += random.choice(["A", "B"])
    for i in range(5):
        string += random.choice(["A", "B"])
    result1 = find_Naive(string, text)
    result2 = find_KMP(string, text)
    result3 = find_KR(string, text, 23)
    assert(result1 == result2 == result3)
