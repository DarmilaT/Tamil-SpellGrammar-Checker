def prefix_match(string1, string2):
    common_length = 0
    min_len = min(len(string1), len(string2))
    for i in range(min_len):
        if string1[i] == string2[i]:
            common_length += 1
        else:
            break
    return common_length

def suffix_match(string1, string2):
    common_length = 0
    min_len = min(len(string1), len(string2))
    for i in range(1, min_len + 1):
        if string1[-i] == string2[-i]:
            common_length += 1
        else:
            break
    return common_length

def prefilter_candidates(user_input, correct_words, length_threshold=2):
    return [
        word for word in correct_words
        if abs(len(word) - len(user_input)) <= length_threshold
    ]


def suggestions(user_input, correct_words):
    suggestions = []
    filtered_correct_words = prefilter_candidates(user_input, correct_words, 2)

    # print(f"Filtered correct words: {filtered_correct_words}")

    for word in filtered_correct_words:
        prefix_score = prefix_match(user_input, word)
        suffix_score = suffix_match(user_input, word)
        score = prefix_score + suffix_score

        if score > 0:
            suggestions.append((word, score))
        
    suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)
    # print(f"Number of Suggestion words: {len(suggestions)}")
    return suggestions
    
