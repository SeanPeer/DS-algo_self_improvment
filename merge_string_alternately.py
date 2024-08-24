def mergeAlternately(word1: str, word2: str):
    flag = True
    i = j = k = 0
    result = ""

    while i < len(word1) and j < len(word2):
        if k % 2 == 0:
            result += word1[i]
            i += 1
        else:
            result += word2[j]
            j += 1
        k += 1

    while i < len(word1):
        result += word1[i]
        i += 1
        k += 1

    while j < len(word2):
        result += word2[j]
        j += 1
        k += 1

    return result


word1 = "abc"
word2 = "pqr"

print(mergeAlternately(word1, word2))
