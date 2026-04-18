# Emotion Detection Application

## Project Overview
This application is designed to detect and analyze human emotions from text, providing insights that can be utilized in various applications, such as customer service, mental health monitoring, and social media analysis.

## Features
- **Real-time Emotion Detection**: Detects emotions from incoming text streams.
- **Supports Multiple Languages**: Capable of processing text in various languages.
- **User-friendly Interface**: Simple API for integration with other applications.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/ADVAIT135/oaqjp-final-project-emb-ai.git
   ```
2. Navigate to the project directory:
   ```bash
   cd oaqjp-final-project-emb-ai
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## API Endpoints
- `POST /detect-emotion`: Detects emotion for a given text.
  - **Request**: JSON object containing the text to analyze.
  - **Response**: Detected emotions with corresponding probabilities.

## Testing Information
To run the tests, execute the following command in the root directory:
```bash
pytest
```
Ensure all tests pass before deployment.

## Acknowledgments
- **Emotion Recognition Models**: Various pre-trained models used in this application.
- **Open Source Libraries**: Thanks to libraries like TensorFlow and scikit-learn for their valuable resources in ML.

---

Last updated on 2026-04-18 10:46:33 UTC.