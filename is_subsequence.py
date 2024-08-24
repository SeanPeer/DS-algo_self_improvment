def is_subsequence(s: str, t: str):
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    j = i = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1

    if i == len(s):
        return True
    else:
        return False


s = "b"
t = "abc"

print(is_subsequence(s, t))
