from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate_spell_checker(test_sentences, expected_corrections, corrected_sentence):
    TP = 0  #True positive - mispelled words that were recognized as mispelled
    FP = 0  #False positive - valid words that were recognized as mispelled
    FN = 0  #False negative - mispelled words that were recognized as correct
    TN = 0  #True negative - valid words that were recognized as correct
    total_words = 0

    for i, sentence in enumerate(test_sentences):
        expected_sentence = expected_corrections[i]

        corrected_words = corrected_sentence.split()
        expected_words = expected_sentence.split()
        test_words = sentence.split()

        for corrected_word, expected_word, test_word in zip(corrected_words, expected_words, test_words):
            total_words += 1
            if test_word == expected_word: #If the input word is correct
                if test_word == corrected_word: #predict as correct word
                    TN += 1
                else: #predict as mispelled word
                    FP += 1
            elif test_word != expected_word: #If the input word is mispelled
                if test_word == corrected_word: #predict as correct word
                    FN += 1
                else: #predict as mispelled word
                    TP += 1

    # Metrics calculations
    accuracy = (TP + TN) / (TP + FP + FN + TN)
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    specificity = TN / (TN + FP) if (TN + FP) != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"Specificity: {specificity}")
    print(f"F1-Score: {f1_score}")