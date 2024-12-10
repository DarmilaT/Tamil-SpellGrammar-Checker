from spell_checker import SpellChecker

correct_words_file = r"D:\7th Semester\AI\Tamil-SpellGrammar-Checker\data\processed\extracted_words.txt"

user_input = "நடைபெறற"

spell_checker = SpellChecker(correct_words_file, user_input)

corrected_text = spell_checker.correct()

# Output the corrected text
print(f"Corrected Text: {corrected_text}")