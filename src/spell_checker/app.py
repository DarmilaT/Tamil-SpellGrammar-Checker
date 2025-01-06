import streamlit as st
from spell_checker import SpellChecker
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Path to the file with correct words
CORRECT_WORDS_FILE = r"D:\7th Semester\AI\Tamil-SpellGrammar-Checker\data\processed\extracted_words.txt"

# Initialize the Streamlit app
st.title("Tamil Spell Checker")
st.write("Enter Tamil text below to check and correct spelling mistakes.")

# Input text box
user_input = st.text_area("Enter Tamil Text:", placeholder="Type your text here...")

# Spell checker functionality
if st.button("Check Spelling"):
    if user_input.strip():
        # Create an instance of the SpellChecker
        spell_checker = SpellChecker(CORRECT_WORDS_FILE, user_input)
        
        # Perform spell checking
        corrected_text = spell_checker.correct()
        
        # Display the corrected text
        st.subheader("Corrected Text:")
        st.write(corrected_text)
    else:
        st.warning("Please enter some text to check spelling.")

# Footer
st.markdown("---")
st.markdown("**Tamil Spell Checker App** - Built with ❤️ using Streamlit")