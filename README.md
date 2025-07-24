# Fraud Detection for E-commerce and Bank Transactions

## Overview
This project aims to improve the detection of fraud cases for e-commerce and bank credit transactions using advanced data analysis, feature engineering, and machine learning models. The solution includes geolocation analysis, transaction pattern recognition, and model explainability.

## Objectives
- Clean and preprocess transaction datasets
- Engineer features to identify fraud patterns
- Build and evaluate Logistic Regression and Ensemble models
- Use SHAP for model explainability
- Ensure code readability, maintainability, and professional repository organization

## Project Structure
```
fraud-detection-ecommerce-bank/
│
├── data/
│   ├── raw/                  # Original datasets
│   └── processed/            # Cleaned/feature-engineered datasets
│
├── notebooks/                # Jupyter notebooks for EDA and prototyping
│
├── src/
│   ├── data/                 # Data loading, cleaning, merging, feature engineering
│   ├── eda/                  # EDA and visualization scripts
│   ├── models/               # Model training, evaluation, explainability
│   └── utils/                # Utility functions
│
├── reports/
│   ├── figures/              # Generated plots and figures
│   └── interim_report.md     # Interim and final reports
│
├── requirements.txt          # Python dependencies
├── .gitignore                # Files/folders to ignore in git
└── README.md                 # Project overview and instructions
```

## Setup Instructions
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place raw datasets in `data/raw/`.
4. Run notebooks or scripts in `src/` as needed.

## Usage
- Use notebooks for EDA and prototyping.
- Use scripts in `src/` for reproducible data processing, modeling, and evaluation.
- Reports and figures are saved in `reports/`.

## Deliverables
- Clean, modular code with documentation
- EDA and modeling results
- SHAP explainability plots
- Interim and final reports

---
For more details, see the interim and final reports in the `reports/` folder.