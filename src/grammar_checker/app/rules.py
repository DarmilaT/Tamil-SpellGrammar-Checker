import re

def tokenize_sentence(sentence):
    """Splits the sentence into words."""
    return sentence.split()

def check_subject_verb_agreement(sentence):
    """
    Rule: Check if the subject agrees with the verb.
    Example:
    'அவள் வந்தான்' -> Incorrect
    'அவள் வந்தாள்' -> Correct
    """
    rules = {
        "அவள்": "வந்தாள்",
        "அவன்": "வந்தான்",
        "அவர்கள்": "வந்தார்கள்",
    }
    tokens = tokenize_sentence(sentence)
    if len(tokens) > 1 and tokens[0] in rules:
        expected_verb = rules[tokens[0]]
        if tokens[1] != expected_verb:
            return f"Error: Expected '{expected_verb}', got '{tokens[1]}'."
    return "No grammatical errors found."
