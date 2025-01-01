import pandas as pd

# Load the dataset
dataset_path = r"D:\7th Semester\AI\Tamil-SpellGrammar-Checker\data\grammar_checker_dataset\tamil_grammar_large_dataset.csv"
df = pd.read_csv(dataset_path)

# Create separate datasets based on 'Error Type' and save them
error_types = df['Error Type'].unique()

output_directory = r"D:\7th Semester\AI\Tamil-SpellGrammar-Checker\data\grammar_checker_dataset"

for error_type in error_types:
    # Filter rows with the current error type
    filtered_df = df[df['Error Type'] == error_type]
    # Generate a filename based on the error type
    filename = f"{error_type.replace(' ', '_')}_dataset.csv"
    output_path = f"{output_directory}\\{filename}"
    # Save the filtered dataset to a CSV file
    filtered_df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Saved {error_type} dataset to {output_path}")