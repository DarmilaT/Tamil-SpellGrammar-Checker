import random

# Define a base set of Tamil sentence templates
sentence_templates = [
    "அவன் புத்தகத்தை படிக்கிறான்.",  # He reads the book. (Accusative case)
    "அவள் பழத்தை சாப்பிடுகிறாள்.",  # She eats the fruit. (Accusative case)
    "நான் பள்ளிக்கு செல்வேன்.",  # I go to school. (Habitual tense)
    "அவர்கள் தினமும் உடற்பயிற்சி செய்கிறார்கள்.",  # They exercise daily. (Habitual tense)
    "பாலன் பந்து விளையாடுவான்.",  # Balan will play ball. (Future tense)
    "பார்வதி வீட்டில் வேலை செய்கிறாள்.",  # Parvathi works at home. (Habitual tense)
    "நான் புத்தகம் படித்தேன்.",  # I read the book. (Past tense)
    "அவள் குழந்தையை பள்ளிக்கு அழைத்துச் செல்கிறாள்.",  # She takes the child to school.
]

# Functions to create random variations
def remove_suffix(sentence):
    """Remove an accusative suffix (-ஐ)."""
    if "ஐ" in sentence:
        return sentence.replace("ஐ", "", 1)
    return sentence

def add_wrong_suffix(sentence):
    """Add a wrong suffix instead of the accusative suffix."""
    if "ஐ" in sentence:
        return sentence.replace("ஐ", "உ", 1)
    return sentence

def modify_tense(sentence):
    """Change the tense randomly."""
    if "றான்" in sentence:
        return sentence.replace("றான்", "ட்டான்")  # Habitual to past
    if "றாள்" in sentence:
        return sentence.replace("றாள்", "ட்டாள்")  # Habitual to past
    if "வேன்" in sentence:
        return sentence.replace("வேன்", "றேன்")  # Future to habitual
    return sentence

# Generate 1000 random sentences
def generate_random_sentences(num_sentences):
    random_sentences = []
    for _ in range(num_sentences):
        sentence = random.choice(sentence_templates)  # Pick a random template
        # Apply random modifications
        modification = random.choice([remove_suffix, add_wrong_suffix, modify_tense, lambda x: x])
        random_sentences.append(modification(sentence))
    return random_sentences

# Generate and shuffle 1000 sentences
random_sentences = generate_random_sentences(1000)
random.shuffle(random_sentences)

# Save to a file
output_file = r"H:\Semester 7\EC9640_Artificial Intelligence\Project\Tamil-SpellGrammar-Checker\data\grammar_checker_dataset\tamil_sentences.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for sentence in random_sentences:
        file.write(sentence + "\n")

print(f"1000 random Tamil sentences saved to {output_file}")
