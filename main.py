
import string
import re
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Ensure all required NLTK resources are available
def download_nltk_resources():
    """Download required NLTK resources if missing."""
    for resource in ["punkt", "punkt_tab"]:
        try:
            nltk.data.find(f"tokenizers/{resource}")
        except LookupError:
            nltk.download(resource)


# Read text from file
def read_text_file(file_path):
  # Reads a text file and returns its content.
  with open(file_path, "r", encoding="utf-8") as file:
    return file.read()


# Method 1: Rule-based analysis
def text_analyzer_rule_based(text):

    text_lower = text.lower()

    # Remove punctuation for word analysis
    text_no_punct = text_lower.translate(
        str.maketrans("", "", string.punctuation)
    )

    words = text_no_punct.split()
    word_count = len(words)

    sentence_count = len(re.findall(r"[.!?]", text))

    top_10_words = Counter(words).most_common(10)

    return {
        "method": "Rule-based",
        "word_count": word_count,
        "sentence_count": sentence_count,
        "top_10_words": top_10_words,
    }


# Method 2: NLTK-based analysis
# Analyze text using NLTK tokenizers.
def text_analyzer_nltk(text):

    # Uses sent_tokenize for sentence detection.
    sentences = sent_tokenize(text)
    sentence_count = len(sentences)

    words = word_tokenize(text.lower())
    words = [w for w in words if w not in string.punctuation]

    word_count = len(words)
    top_10_words = Counter(words).most_common(10)

    return {
        "method": "NLTK",
        "word_count": word_count,
        "sentence_count": sentence_count,
        "top_10_words": top_10_words,
    }

# Main
if __name__ == "__main__":
    download_nltk_resources()

    FILE_PATH = "/content/sample_text.txt"
    text = read_text_file(FILE_PATH)

    rule_based_result = text_analyzer_rule_based(text)
    nltk_result = text_analyzer_nltk(text)

    # Display results
    for result in [rule_based_result, nltk_result]:
        print(f"\n=== {result['method']} Analysis ===")
        print("Word count:", result["word_count"])
        print("Sentence count:", result["sentence_count"])
        print("Top 10 most frequent words:")
        for word, freq in result["top_10_words"]:
            print(f"  {word}: {freq}")