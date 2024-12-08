def levenshtein_distance(string1, string2):
    
    n, m = len(string1), len(string2)
    # Declaring array 'dp' with rows = len(string1) + 1 and columns = len(string2) + 1:
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialising first row:
    for i in range(n + 1):
        dp[i][0] = i
    # Initialising first column:
    for j in range(m + 1):
        dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Adding 1 to account for the cost of operation:
                insertion = 1 + dp[i][j-1]
                deletion = 1 + dp[i-1][j]
                replacement = 1 + dp[i-1][j-1]

                dp[i][j] = min(insertion, deletion, replacement)
    
    return dp[n][m]

def find_closest_levenshtein(user_input, correct_words):
    return min(correct_words, key=lambda word: levenshtein_distance(user_input, word))






