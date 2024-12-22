# Tamil Spell and Grammar Checker

This project aims to build a Tamil Spell and Grammar Checker using a combination of traditional and modern approaches. The system is divided into two main components: **Spell Checker** and **Grammar Checker**.

## Features

1. **Spell Checker**

   - Suggests corrections based on prefix and suffix similarity.
   - Employs Levenshtein Distance for accurate word correction.
   - Processes a large corpus of Tamil words from Kaggle datasets.

2. **Grammar Checker**
   - Handles habitual tense rules.
   - Checks subject-verb agreement.
   - Implements rule-based, machine learning (Random Forest), and deep learning approaches.

## Methods and Workflow

### Spell Checker

1. **Data Collection and Preprocessing**

   - Used Tamil paragraph datasets from Kaggle.
   - Extracted and cleaned nearly 1 lakh unique words from the dataset.
   - Preprocessed text by tokenizing and normalizing words.

2. **Prefix and Suffix Suggestion**

   - Before applying Levenshtein Distance, the system generates word suggestions based on prefix and suffix matching to improve performance and reduce computational complexity.
   - Example: For the input "அரசன", the system might suggest "அரசன்", "அரசின்", etc.

3. **Levenshtein Distance**

   - Calculates the minimum edit distance between the input word and valid Tamil words.
   - Suggests the most probable correct word based on the smallest edit distance.

4. **Evaluation Metrics**
   - **Accuracy**: Proportion of correctly identified words.
   - **Precision**: Correct suggestions out of all suggestions made.
   - **Recall**: Correct suggestions out of all possible corrections.
   - **F1 Score**: Balances precision and recall.

### Grammar Checker

1. **Rules Implemented**

   - **Habitual Tense Rule**: Ensures habitual actions follow correct tense forms
   - **Subject-Verb Agreement**: Validates that the verb matches the subject's form
   - Here is the table format with more examples for the rules implemented:

   | **Rule**                   | **Valid Example**                          | **Invalid Example**                        | **Explanation**                                               |
   | -------------------------- | ------------------------------------------ | ------------------------------------------ | ------------------------------------------------------------- |
   | **Habitual Tense Rule**    | நான் தினமும் ஐந்து மணிக்கு எழுந்திருப்பேன் | நான் தினமும் ஐந்து மணிக்கு எழுந்திருகிறேன் | Ensures habitual actions are in the correct future tense.     |
   | **Subject-Verb Agreement** | அவன் படித்தான்                             | அவன் படிக்கிறேன்                           | Verbs must agree with the subject in terms of tense and form. |
   | **Habitual Tense Rule**    | நான் தினமும் தேநீர் குடிப்பேன்             | நான் தினமும் தேநீர் குடித்தேன்             | Ensures habitual action of future tense with correct verb.    |
   | **Subject-Verb Agreement** | நான் மரத்தை வெட்டினேன்                     | நான் மரத்தை வெட்டினான்                     | Verbs must agree with the subject in terms of tense and form. |

2. **Approaches Used**

   - **Rule-Based Approach**:
     - Hard-coded grammar rules.
     - Useful for highly structured and deterministic checks.
   - **Machine Learning Approach**:
     - Used a Random Forest classifier to learn and predict grammatical correctness.
     - Required labeled dataset with examples of correct and incorrect Tamil grammar usage.
   - **Deep Learning Approach**:
     - Trained a simple LSTM model to detect grammatical errors in sentences.
     - Captures contextual dependencies in Tamil sentences.

3. **Evaluation**
   - Models were evaluated using the same metrics as the spell checker: accuracy, precision, recall, and F1 score.

## Contributors

- **Darmila.T**
- **Mayrariniy.CJ**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
