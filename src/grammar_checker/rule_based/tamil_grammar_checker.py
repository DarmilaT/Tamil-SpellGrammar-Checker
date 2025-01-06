from tamil_grammar_rules import check_subject_verb_agreement, check_habitual_case

# Combined Grammar Checker
def grammar_checker(sentence):
    subject_verb_result, corrected_subject_verb = check_subject_verb_agreement(sentence)
    habitual_case_result, corrected_habitual = check_habitual_case(sentence if not corrected_subject_verb else corrected_subject_verb)

    # If corrections are made, return the corrected sentence
    corrected_sentence = corrected_habitual if corrected_habitual else corrected_subject_verb
    return subject_verb_result, habitual_case_result, corrected_sentence if corrected_sentence else sentence

# Test Sentences
test_sentences = [
    "அவன் பாடம் படிக்கிறான்",  # Correct subject-verb agreement
    "அவர்கள் பாடம் படிக்கிறான்",  # Incorrect subject-verb agreement
    "நான் தினமும் எழுந்து விடுவேன்",  # Correct habitual case with compound verb
    "நாம் தினசரி விளையாடுகிறோம்",  # Correct subject-verb, incorrect habitual case
    #"அவள் தினமும் தேநீர் குடிக்கிறாள்",  # Present tense acceptable for habitual case
    "மாணவர்கள் பாடம் படிக்கிறார்கள்",  # Correct subject-verb agreement
<<<<<<< HEAD
    "அவர்கள் விளையாட்டு விளையாடுகிறேன்"
=======
>>>>>>> 757cc1cd0403d1336e16bf1c11653bd4c71efbc8
]

if __name__ == "__main__":
    for i, sentence in enumerate(test_sentences, 1):
        print(f"Sentence {i}: {sentence}")
        subject_verb_result, habitual_case_result, corrected_sentence = grammar_checker(sentence)
        print(subject_verb_result)
        print(habitual_case_result)
        if sentence != corrected_sentence:
            print(f"Corrected Sentence: {corrected_sentence}")
        print("-" * 50)