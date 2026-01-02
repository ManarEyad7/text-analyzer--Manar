# Text Analyzer

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

- Example Output
=== Rule-based Analysis ===
Word count: 181
Sentence count: 38
Top 10 most frequent words:
  and: 9
  ai: 6
  we: 6
  repeat: 5
  is: 4
  are: 4
  to: 2
  2026: 2
  ship: 2
  test: 2

=== NLTK Analysis ===
Word count: 195
Sentence count: 28
Top 10 most frequent words:
  and: 9
  we: 7
  ai: 6
  is: 5
  repeat: 5
  are: 4
  n't: 3
  hello: 2
  to: 2
  2026: 2
