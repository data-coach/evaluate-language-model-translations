# Evaluate Language Model Translations Using BLEU and ROUGE Scores

## Description

This repository demonstrates how to evaluate language model translations using **BLEU** and **ROUGE** metrics. It provides a practical implementation with Python, utilizing the **H2OGPTE** client for translation and the `nltk` and `rouge-score` libraries for evaluation. The project highlights the advantages, limitations, and interpretation of these metrics for assessing the quality of machine-generated translations.

## Features

- Translate text from English to a target language using the H2OGPTE API.  
- Calculate BLEU and ROUGE scores for translation evaluation.  
- Understand the strengths and limitations of BLEU and ROUGE metrics.  
- Example dataset for testing and evaluation.

## Requirements

- Python 3.8+
- Required Python packages:  
  ```bash
  pip install h2ogpte nltk rouge-score
  ```
- NLTK resources:  
  ```python
  import nltk
  nltk.download('punkt')
  ```

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/evaluate-language-model-translations.git
   cd evaluate-language-model-translations
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up H2OGPTE API keys in a `config.py` file:
   ```python
   H2O_GPT_E_API_KEY = "your_api_key_here"
   REMOTE_ADDRESS = "your_h2ogpte_server_address"
   ```

4. Run the script to translate and evaluate:
   ```bash
   python evaluate_translations.py
   ```

## Example Output

```text
Source: How are you?
Reference: ¿Cómo estás?
Candidate: ¿Cómo estás?
Metrics: {'BLEU': 0.221, 'ROUGE-1': 1.0, 'ROUGE-2': 1.0, 'ROUGE-L': 1.0}

Source: What is your name?
Reference: ¿Cómo te llamas?
Candidate: ¿Cuál es tu nombre?
Metrics: {'BLEU': 0.0, 'ROUGE-1': 0.67, 'ROUGE-2': 0.50, 'ROUGE-L': 0.60}
```

## Contributing

Feel free to contribute by submitting issues or pull requests to improve the repository.

## License

This project is licensed under the [MIT License](LICENSE).
