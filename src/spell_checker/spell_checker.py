from algorithms import suggestions, find_closest_levenshtein

class SpellChecker:
    def __init__(self, correct_words_file, user_input):
        self.user_input_words = user_input.split()
        with open(correct_words_file, 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.correct_words = list(data)
    
    def correct(self):
        corrected_words = []
        for word_to_check in self.user_input_words:
            suggested_words = suggestions(word_to_check, self.correct_words)

            # print(f"Number of Suggested words for {word_to_check} -> {len(suggested_words)}")

            # find the corrected word
            best_match = find_closest_levenshtein(word_to_check, suggested_words)
            corrected_word = best_match[0].strip()
            corrected_words.append(corrected_word)

            # print(corrected_words)

        return " ".join(corrected_words)