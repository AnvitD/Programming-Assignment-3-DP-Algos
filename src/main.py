import os
import glob

def find_highest_value_lcs(weights: dict, str_a: str, str_b: str):
    n, m = len(str_a), len(str_b)
    dp_table = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            char_a, char_b = str_a[i - 1], str_b[j - 1]
            if char_a == char_b:
                val = weights.get(char_a, 0)
                dp_table[i][j] = dp_table[i - 1][j - 1] + val
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

    lcs_chars = []
    i, j = n, m
    while i > 0 and j > 0:
        if str_a[i - 1] == str_b[j - 1]:
            lcs_chars.append(str_a[i - 1])
            i -= 1
            j -= 1
        elif dp_table[i - 1][j] >= dp_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp_table[n][m], "".join(reversed(lcs_chars))
