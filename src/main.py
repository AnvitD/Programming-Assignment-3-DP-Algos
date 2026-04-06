import os
import glob

def parse_input(raw_data: str):
    lines = [line.strip() for line in raw_data.strip().splitlines() if line.strip()]
    
    if not lines:
        return {}, "", ""

    try:
        num_values = int(lines[0])
        char_weights = {}
        for i in range(1, num_values + 1):
            char, weight = lines[i].split()
            char_weights[char] = int(weight)
        
        string_a = lines[num_values + 1] if len(lines) > num_values + 1 else ""
        string_b = lines[num_values + 2] if len(lines) > num_values + 2 else ""
        
        return char_weights, string_a, string_b
    except (ValueError, IndexError) as e:
        return {}, "", ""

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
