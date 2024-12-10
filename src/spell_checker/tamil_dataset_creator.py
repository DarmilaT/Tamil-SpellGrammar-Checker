import pandas as pd
import re
from pathlib import Path

def load_dataset(file_path):
    if not Path(file_path).exists():
        raise FileNotFoundError(f"Dataset not found at {file_path}")
    return pd.read_csv(file_path)

def extract_words_from_text(text):
    text = re.sub(r'[0-9\.]', '', text)
    # Remove any special characters or punctuation (except Tamil letters and spaces)
    text = re.sub(r'[^\u0B80-\u0BFF\s]', '', text)
    words = text.split()  # Splits by spaces
    return words

def extract_words_from_dataset(dataset):
    all_words = []
    for text in dataset['text']:
        words = extract_words_from_text(text)
        all_words.extend(words)
    return all_words

def save_words_to_file(words, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

if __name__ == "__main__":

    dataset_path = r"D:\7th Semester\AI\Tamil-SpellGrammar-Checker\data\raw\tamil_dataset.csv" 
    output_file = r"D:\7th Semester\AI\Tamil-SpellGrammar-Checker\data\processed\extracted_words.txt" 

    # Load dataset
    print("Loading dataset...")
    dataset = load_dataset(dataset_path)

    # Extract words
    print("Extracting words...")
    extracted_words = extract_words_from_dataset(dataset)

    # Save extracted words
    print(f"Saving words to {output_file}...")
    save_words_to_file(extracted_words, output_file)

    print(f"Extracted {len(extracted_words)} words successfully!")
