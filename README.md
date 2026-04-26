# Social Engineering Email Detection System 🛡️

AI-powered detection system for Phishing, Business Email Compromise (BEC), and Fraudulent emails, with a specific focus on identifying **Nigerian and African-centric scam patterns**.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Key Features

*   **Deep Learning Detection**: Utilizes a fine-tuned DistilBERT model achieving ~99.5% accuracy.
*   **Regional Context**: Specially trained on Nigerian scam patterns (inheritance, advance fee fraud, urgent financial baits).
*   **Zero-Day Defense**: Rule-based heuristic engine to catch new variants before model retraining.
*   **Explainable AI (XAI)**: Integrated SHAP support to provide transparency on why an email was flagged.
*   **Production Pipeline**: Ready-to-use inference scripts for real-time scanning.

## 📁 Repository Structure

*   `sed_full_implementation.ipynb`: Complete research, EDA, and model training workflow.
*   `pipeline.py`: The core inference logic and feature extraction.
*   `predict.py`: CLI tool for testing individual emails.
*   `data/`: (Local only) Raw and processed datasets.
*   `models/`: (Local only) Saved model weights (Random Forest, DistilBERT, etc.).

## 🚀 Getting Started

### 1. Installation

```bash
# Clone the repository
git clone <your-repository-link>
cd social-engineering-detection

# Install dependencies
pip install -r requirements.txt
```

### 2. Quick Usage

You can run the prediction system directly from your terminal:

```bash
python predict.py
```

Or integrate it into your code:

```python
from pipeline import predict_email

email_text = "Urgent: Your account is suspended. Click here to verify your identity."
result = predict_email(email_text)

print(result['verdict'])
# Output: 🚨 PHISHING / SOCIAL ENGINEERING
```

## ⚠️ Important Note on Data & Models

Due to GitHub's file size limitations (100MB), the large dataset files and trained model binaries (`.pkl`, `.pth`) are **not included** in this repository. 

To use the system:
1. Run the `sed_full_implementation.ipynb` notebook to download the datasets and train the models locally.
2. The notebook will automatically create the `models/` folder and save the required assets.

## 📊 Dataset Sources

The models are trained on a unified corpus compiled from the following Kaggle datasets:

1.  **[Fraudulent Email Corpus](https://www.kaggle.com/datasets/rtatman/fraudulent-email-corpus)**: A collection of "419" Nigerian Advance Fee Fraud emails.
2.  **[Adversarial BEC Dataset](https://www.kaggle.com/datasets/yoadjei/adversarial-bec-email-dataset)**: Targeted Business Email Compromise patterns.
3.  **[Phishing Email Dataset](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset)**: A broad collection of general phishing attempts.
4.  **[Phishing and Legitimate Emails](https://www.kaggle.com/datasets/kuladeep19/phishing-and-legitimate-emails-dataset)**: Balanced synthetic and real-world email data.

## 🛠️ Future Work

- [ ] **Browser Extension**: Real-time phishing protection for webmail.
- [ ] **Federated Learning**: Privacy-preserving training across multiple organizations.
- [ ] **API Endpoint**: RESTful API for easy enterprise integration.

---
**Note:** Training deep learning models like DistilBERT is highly recommended on a GPU for optimal performance.