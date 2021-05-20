# naive algorithm
def find_Naive(string, text):
    result = []
    string_len = len(string)
    text_len = len(text)
    if text_len == 0 or string_len == 0:
        return result
    # loop for searching the text one by one
    for i in range(text_len - string_len + 1):
        j = 0
        while(j < string_len):
            if (text[i + j] != string[j]):
                break
            j += 1
        if (j == string_len):
            result.append(i)
    return result


# Knuth Morris Pratt algorithm
def find_KMP(string, text):
    string_len = len(string)
    text_len = len(text)
    result = []
    if text_len == 0 or string_len == 0:
        return result
    # pre_suf_list[] with the longest prefix suffix values for pattern
    pre_suf_list = [0]*string_len

    compute_ps_list(string, string_len, pre_suf_list)
    j = 0
    i = 0
    while i < text_len:
        if string[j] == text[i]:
            i += 1
            j += 1

        if j == string_len:
            result.append(i-j)
            j = pre_suf_list[j-1]

        elif i < text_len and string[j] != text[i]:
            if j != 0:
                j = pre_suf_list[j-1]
            else:
                i += 1
    return result


# function to create a list with the longest prefix suffix values in the string
def compute_ps_list(string, string_len, ps_list):

    len = 0
    ps_list[0] = 0
    i = 1

    while i < string_len:
        if string[i] == string[len]:
            len += 1
            ps_list[i] = len
            i += 1
        else:
            if len != 0:
                len = ps_list[len-1]
            else:
                ps_list[i] = 0
                i += 1
