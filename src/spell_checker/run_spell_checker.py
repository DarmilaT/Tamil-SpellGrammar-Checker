from spell_checker import SpellChecker
from tests.spell_checker_evaluator import evaluate_spell_checker

correct_words_file = r"D:\7th Semester\AI\Tamil-SpellGrammar-Checker\data\processed\extracted_words.txt"

test_paragrapgh = "ஏற்றுமதயை நம்பியுள்ள நாடுகளுகுத்தான் இதனால் பாதிப்பு. உள்நாட்டிலேயே தேவை அதிகமக உள்ள இந்தியா போன்ற மக்கள் தொகை அதிகம் கொண்ட வளரும் பொருளதர நாட்டில் பிரச்சனை ஏற்படது என்று அவர் திடவட்டமாகக் கூறினார்."
expected_paragrapgh = "ஏற்றுமதியை நம்பியுள்ள நாடுகளுக்குத்தான் இதனால் பாதிப்பு. உள்நாட்டிலேயே தேவை அதிகமாக உள்ள இந்தியா போன்ற மக்கள் தொகை அதிகம் கொண்ட வளரும் பொருளாதார நாட்டில் பிரச்சனை ஏற்படாது என்று அவர் திட்டவட்டமாகக் கூறினார்."

test_sentences = test_paragrapgh.rstrip(".").split(".")
expected_sentences = expected_paragrapgh.rstrip(".").split(".")

for i, sentence in enumerate(test_sentences):
    print(f"\n\nTest Sentence: {sentence}")
    spell_checker = SpellChecker(correct_words_file, sentence)
    corrected_text = spell_checker.correct()

    # Output the corrected text
    print(f"Corrected Text: {corrected_text}\n")

    # Evaluate the spell checker
    evaluate_spell_checker(corrected_text, expected_sentences[i], corrected_text)