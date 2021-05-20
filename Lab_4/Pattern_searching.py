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


# Karp-Rabin algorithm
def find_KR(string, text, q):
    d = 32  # numbers of chars in the alphabet
    result = []
    string_len = len(string)
    text_len = len(text)
    i = 0
    j = 0
    hash_s = 0    # stores hash value for string
    hash_t = 0    # stores hash value for text
    h = 1
    # check if txt or pattern is empty or txt < pat
    if string_len == 0 or text_len == 0 or text_len < string_len:
        return result

    for i in range(string_len - 1):
        h = (h * d) % q

    # The ord() function accepts a string of length 1 as an argument
    # and returns the unicode code point representation
    # Calculate the hash value for pattern and first text window:
    for i in range(string_len):
        hash_s = (d * hash_s + ord(string[i])) % q
        hash_t = (d * hash_t + ord(text[i])) % q

    # Find the match:
    for i in range(text_len-string_len + 1):
        # Check the hash values of current window of text and pattern
        if hash_s == hash_t:
            # If the hash values match then check for characters on by one
            for j in range(string_len):
                if text[i + j] != string[j]:
                    break
            j += 1
            if j == string_len:
                # print "Pattern found at index " + str(i)
                result.append(i)

        # Calculate hash value for next window of text
        if i < text_len - string_len:
            hash_t = (d * (hash_t - ord(text[i]) * h) + ord(text[i + string_len])) % q

            # If we get negative value - convert t to positive
            if hash_t < 0:
                hash_t = hash_t + q

    return result
