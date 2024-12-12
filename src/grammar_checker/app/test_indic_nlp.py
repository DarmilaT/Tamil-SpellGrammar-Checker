import os
from indicnlp.tokenize import sentence_tokenize

# Set the path to Indic NLP Resources
os.environ["INDIC_RESOURCES_PATH"] = "H:\Semester 7\EC9640_Artificial Intelligence\Project\indic_nlp_resources"

# Tamil text for testing
text = "அவள் பள்ளிக்குச் சென்றாள். அவள் தனது வகுப்பறையில் இருந்தாள்."

# Sentence tokenization
sentences = sentence_tokenize.sentence_split(text, lang='ta')

# Print the tokenized sentences
print(sentences)
