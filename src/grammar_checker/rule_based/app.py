import streamlit as st
from tamil_grammar_rules import check_subject_verb_agreement, check_habitual_case

# Grammar Checker Function
def grammar_checker(sentence):
    subject_verb_result, corrected_subject_verb = check_subject_verb_agreement(sentence)
    habitual_case_result, corrected_habitual = check_habitual_case(
        sentence if not corrected_subject_verb else corrected_subject_verb
    )

    # If corrections are made, return the corrected sentence
    corrected_sentence = corrected_habitual if corrected_habitual else corrected_subject_verb
    return subject_verb_result, habitual_case_result, corrected_sentence if corrected_sentence else sentence

# Streamlit App
st.title("Tamil Grammar Checker - Paragraph Analysis")
st.write("Enter a Tamil paragraph to analyze grammar issues sentence by sentence.")

# Input text box
paragraph_input = st.text_area(
    "Enter Tamil Paragraph:",
    placeholder="Type or paste a paragraph here...",
    height=200,
)

# Analyze button
if st.button("Analyze Paragraph"):
    if paragraph_input.strip():
        # Split input into paragraphs (if multiple paragraphs are provided)
        paragraphs = paragraph_input.split("\n")

        # Iterate over paragraphs
        for i, paragraph in enumerate(paragraphs):
            st.subheader(f"Paragraph {i+1}:")
            st.write(paragraph)

            # Split paragraph into sentences
            sentences = paragraph.split(". ")
            
        # Analyze each sentence in a paragraph
        for j, sentence in enumerate(sentences):
            if sentence.strip():  # Ignore empty sentences
                subject_verb_result, habitual_case_result, corrected_sentence = grammar_checker(sentence)

                # Add a clear separation for each sentence
                st.markdown(f"### Sentence {j+1}:")
                st.markdown(f"> **Original Sentence:** {sentence}")

                # Display subject-verb agreement result
                if subject_verb_result:
                    st.warning(f"**Subject-Verb Agreement Issue:** {subject_verb_result}")
                else:
                    st.success("**Subject-Verb Agreement:** No issues detected.")

                # Display habitual case result
                if habitual_case_result:
                    st.warning(f"**Habitual Case Issue:** {habitual_case_result}")
                else:
                    st.success("**Habitual Case:** No issues detected.")

                # Highlight corrections if needed
                if sentence != corrected_sentence:
                    st.markdown(
                        f"""<div style="background-color:#f9f9f9; padding:10px; border-left: 5px solid #ff4b4b;">
                        <strong>Suggested Correction:</strong> {corrected_sentence}
                        </div>""",
                        unsafe_allow_html=True,
                    )
                else:
                    st.success("No corrections needed!")

                # Add a separator between sentences
                st.markdown("---")

    else:
        st.warning("Please enter a paragraph to analyze.")

# Footer
st.markdown("---")
st.markdown("**Tamil Grammar Checker** - Built with ❤️ using Streamlit")