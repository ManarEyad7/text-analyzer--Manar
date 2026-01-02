# Text Analyzer (Rule-based & NLTK)

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
  
