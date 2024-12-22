# Rule 1: Subject-Verb Agreement Checker
def check_subject_verb_agreement(sentence):
    singular_subjects = ["அவன்", "அவள்", "இவன்", "இவள்", "நான்"]
    plural_subjects = ["அவர்கள்", "மாணவர்கள்", "நாம்", "நாங்கள்", "அவைகள்"]

    singular_verbs = ["கிறான்", "கிறாள்", "றான்", "றாள்", "வேன்"]
    plural_verbs = ["கிறார்கள்", "கிறோம்", "றார்கள்", "றோம்", "வோம்"]

    words = sentence.split()
    subject = None
    verb = None

    for word in words:
        if word in singular_subjects or word in plural_subjects:
            subject = word
        elif any(word.endswith(ending) for ending in singular_verbs + plural_verbs):
            verb = word

    if not subject or not verb:
        return "Unable to determine subject or verb.", None

    if subject in singular_subjects and any(verb.endswith(ending) for ending in plural_verbs):
        corrected = sentence.replace(verb, verb.rstrip("கிறார்கள்") + "கிறான்")
        return f"Singular subject '{subject}' must have a singular verb. Found '{verb}'.", corrected
    elif subject in plural_subjects and any(verb.endswith(ending) for ending in singular_verbs):
        corrected = sentence.replace(verb, verb.rstrip("கிறான்") + "கிறார்கள்")
        return f"Plural subject '{subject}' must have a plural verb. Found '{verb}'.", corrected

    return "Correct.", None


# Rule 2: Habitual Case Checker
def check_habitual_case(sentence):
    habitual_indicators = ["தினமும்", "நாட்தோறும்", "தினசரி"]
    habitual_verbs = ["வேன்", "வோம்", "வார்", "வாய்", "வாள்"]
    present_tense_verbs = ["கிறேன்", "கிறோம்", "கிறாள்", "கிறார்கள்"]

    words = sentence.split()
    if any(indicator in sentence for indicator in habitual_indicators):
        for word in words:
            if any(word.endswith(ending) for ending in habitual_verbs):
                return "Habitual Case: Correct.", None
            elif any(word.endswith(ending) for ending in present_tense_verbs):
                corrected = sentence.replace(word, word.rstrip("கிறேன்") + "வேன்")
                return "Habitual Case: Error - Present tense verb used for habitual action.", corrected

    return "Not applicable.", None
