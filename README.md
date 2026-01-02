# Text Analyzer
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11rsVSMS2WEQsrVraUNC4O4LBlNpXbcvq?usp=sharing)

This project analyzes a text file using **two different methods**:

1. **Rule-based approach**
   - Uses regex and string processing
   - Sentences are counted by `.`, `!`, `?`

2. **NLTK-based approach**
   - Uses `nltk.sent_tokenize` for more accurate sentence detection

For each method, the script outputs:
- Word count
- Sentence count
- Top 10 most frequent words (ignoring punctuation)

---

How to Run

- Place your text inside sample_text.txt

   - Make sure the file path in the code matches your file location:
   - FILE_PATH = "/content/sample_text.txt"

- Run the script:
   - python analyzer.py
