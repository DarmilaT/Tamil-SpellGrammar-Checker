import pandas as pd
import re

# Step 1: Load the dataset
file_path = r"H:\Semester 7\EC9640_Artificial Intelligence\Project\Tamil-SpellGrammar-Checker\data\raw\tamil_dataset.csv" 
tamil_dataset = pd.read_csv(file_path)

# Step 2: Define a function to split paragraphs into sentences
def split_into_sentences(paragraph):
    # Use Tamil punctuation marks for splitting
    sentences = re.split(r'[.!?]', str(paragraph))  # Adjust pattern for additional delimiters if needed
    # Remove empty strings and strip leading/trailing spaces
    return [sentence.strip() for sentence in sentences if sentence.strip()]

# Step 3: Extract sentences from the 'text' column
all_sentences = []
for paragraph in tamil_dataset['text']:
    all_sentences.extend(split_into_sentences(paragraph))

# Step 4: Save sentences to a text file
output_file = r"H:\Semester 7\EC9640_Artificial Intelligence\Project\Tamil-SpellGrammar-Checker\data\grammar_checker_dataset\extracted_tamil_sentences.txt"
with open(output_file, 'w', encoding='utf-8') as f:
    for sentence in all_sentences:
        f.write(sentence + '\n')

print(f"Extracted sentences saved to: {output_file}")
