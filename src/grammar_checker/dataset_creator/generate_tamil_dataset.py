import pandas as pd
import random

# Define subjects, verbs, objects, and templates
subjects = ["நான்", "அவன்", "அவள்", "நாம்", "அவர்கள்", "பார்வதி"]
objects = ["பள்ளிக்கு", "புத்தகத்தை", "பழத்தை", "பந்து", "வீட்டில்", "பாடத்தை"]
actions_correct = ["செல்வேன்", "படிக்கிறான்", "படிக்கிறாள்", "விளையாடுகிறோம்", "சாப்பிடுகிறான்"]
actions_incorrect = ["செல்கிறான்", "படிக்கிறார்கள்", "சாப்பிடுகிறாள்", "விளையாடுகிறான்", "சாப்பிடுவாள்"]
error_types = ["Subject-Verb Agreement", "Habitual Case", "Verb Tense", "Spelling Error"]

# Generate logical dataset
data = []
for _ in range(5000):  # Adjust the number as needed
    subject = random.choice(subjects)
    obj = random.choice(objects)
    correct_action = random.choice(actions_correct)
    incorrect_action = random.choice(actions_incorrect)
    error_type = random.choice(error_types)

    # Create sentences
    correct_sentence = f"{subject} {obj} {correct_action}."
    incorrect_sentence = f"{subject} {obj} {incorrect_action}."

    # Randomly assign errors
    if random.random() > 0.5:
        data.append({
            "Sentence": incorrect_sentence,
            "Error Type": error_type,
            "Corrected Sentence": correct_sentence
        })
    else:
        data.append({
            "Sentence": correct_sentence,
            "Error Type": "No Error",
            "Corrected Sentence": correct_sentence
        })

# Convert to DataFrame
logical_dataset = pd.DataFrame(data)

# Save the dataset
dataset_path = "H:/Semester 7/EC9640_Artificial Intelligence/AI Project/Tamil-SpellGrammar-Checker/data/grammar_checker_dataset/tamil_grammar_large_dataset.csv"
logical_dataset.to_csv(dataset_path, index=False)

print(f"Dataset successfully saved at: {dataset_path}")

