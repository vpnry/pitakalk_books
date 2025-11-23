# Pitaka.lk Typed Books (Offline English Translations)

This repository hosts AI English translations of Sinhala Buddhist books, originally sourced from [pitaka.lk](https://pitaka.lk/books/). 

## Translated Books

Currently, the following books have been translated:

1.  **Abhidharma Margaya**: Located in the `abhidharma-margaya-en` directory.
    -   **Translation Engine**: Gemini 3.0 Pro (High) via Antigravity (agent).
    -   **Note**: The translation quality could be improved. The current version was translated from individual files. A better result was achieved in testing by using a combined Markdown file ([`complete_sinhala_combined_book.md`](dev/abhidharma-margaya-strip-icon/complete_sinhala_combined_book.md)) and providing `A Comprehensive Manual of Abhidhamma` (ISBN: 978-955-24-0103-9) as a reference for English terminology.
    -   The prompt used for the translation is available [here](./dev/abhidharma-margaya-strip-icon/prompt.md).

**Important:** The English translations in this repository were generated using Large Language Models (LLMs) and have not yet been proofread by a human. As a result, they may contain errors or inaccuracies. Please exercise caution and discernment when reading.


## Repository Structure

```
.
├── abhidharma-margaya-en/  # English translation of Abhidharma Margaya
├── common/                   # Shared CSS, JS, and font files for book styling
├── origin_sinhala/           # Original Sinhala books from pitaka.lk
└── README.md                 # This file
```

## Attributions

The original Sinhala books in the `origin_sinhala` directory are from [pitaka.lk](https://pitaka.lk/books/). We are grateful for their work in making these texts available.