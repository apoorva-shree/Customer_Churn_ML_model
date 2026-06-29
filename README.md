# 📊 Customer Churn Prediction & Retention Analytics

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

</p>

---

# 🚀 Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses and telecom companies. Acquiring a new customer is significantly more expensive than retaining an existing one.

This project builds an **end-to-end Machine Learning pipeline** that predicts whether a customer is likely to churn and provides **actionable business insights** to improve customer retention strategies.

The project goes beyond model building by answering:

- **Who is likely to leave?**
- **Why are they leaving?**
- **What actions can the business take to retain them?**

---

# 🎯 Business Objective

Develop a predictive system that helps companies:

✅ Identify high-risk customers.

✅ Understand the drivers behind customer attrition.

✅ Build targeted retention campaigns.

✅ Reduce revenue loss due to churn.

---

# 💼 Skills Demonstrated

This project showcases proficiency in:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Handling Imbalanced Data (SMOTE)
- Machine Learning Model Building
- Cross Validation
- Model Evaluation
- Feature Importance Analysis
- Business Analytics
- Model Serialization (Pickle)
- Streamlit Deployment
- End-to-End ML Project Development

---

# 🛠 Tech Stack

| Category | Tools |
|----------|--------|
| Language | Python |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn |
| Imbalanced Learning | SMOTE |
| Models | Random Forest, Decision Tree, XGBoost |
| Deployment | Streamlit |
| Environment | Jupyter Notebook |

---

# 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

**Features:** 20+

**Target Variable:** Churn (Yes / No)

The dataset contains customer demographic information, subscription details, billing information, and service usage patterns.

---

# 🔬 Project Workflow

```text
Raw Data
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Encoding
   ↓
Train-Test Split
   ↓
SMOTE (Class Balancing)
   ↓
Model Training
   ↓
Cross Validation
   ↓
Model Evaluation
   ↓
Feature Importance Analysis
   ↓
Business Insights
   ↓
Deployment using Streamlit
```

---

# 📊 Exploratory Data Analysis

The project includes extensive EDA to understand customer behavior and churn patterns.

### Key Analyses Performed

- Churn Distribution
- Numerical Feature Analysis
- Correlation Heatmap
- Contract Type Analysis
- Monthly Charges Analysis
- Total Charges Analysis
- Tenure Analysis
- Customer Segmentation

---

# 🤖 Machine Learning Models Tested

| Model | Purpose |
|-------|----------|
| Decision Tree | Baseline Model |
| Random Forest | Final Model |
| XGBoost | Performance Comparison |

Cross-validation was performed to compare the models and select the best-performing algorithm.

---

# 🏆 Final Model

### Random Forest Classifier

Chosen because it delivered the best balance between performance and generalization.

---

# 📈 Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | 77.86% |
| Precision | 0.58 |
| Recall | 0.59 |
| F1 Score | 0.58 |
| Weighted F1 | 0.78 |

---

# 📊 Model Evaluation

## Confusion Matrix

<p align="center">
<img src="Images/confusion_matrix.png" width="550">
</p>

---

## ROC Curve & AUC

<p align="center">
<img src="Images/ROC_curve and AUC score.png" width="550">
</p>

---

# 🔥 Feature Importance

<p align="center">
<img src="Images/Top 10 imp features.png" width="700">
</p>

The model identified the most influential factors affecting customer churn.

### Top Drivers of Churn

- Contract Type
- Tenure
- Monthly Charges
- Total Charges
- Internet Service
- Payment Method

---

# 📌 Key Insights

### Customers most likely to churn:

✔️ Month-to-Month contract customers

✔️ Customers with short tenure

✔️ Customers with high monthly charges

✔️ Newly acquired customers

---

# 💡 Business Recommendations

### 1. Promote Long-Term Contracts
Offer discounts to customers willing to switch to yearly plans.

### 2. Retain New Customers
Launch onboarding and engagement campaigns during the first few months.

### 3. Target High-Bill Customers
Provide personalized offers and loyalty discounts.

### 4. Build Early Warning Systems
Use predictive analytics to proactively contact at-risk customers.

### 5. Increase Customer Lifetime Value
Implement reward programs and personalized retention strategies.

---

# 🌐 Deployment

The trained model was:

✅ Serialized using Pickle

✅ Integrated into a Streamlit application

✅ Deployed as an interactive churn prediction tool

Users can input customer information and instantly receive churn predictions.

---

# 📁 Repository Structure

```text
Customer-Churn-Prediction
│
├── Customer_Churn_ML_final.ipynb
├── app.py
├── customer_churn.pkl
├── encoders.pkl
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── requirements.txt
├── README.md
│
└── Images/
      ├── confusion_matrix.png
      ├── ROC_curve and AUC score.png
      └── Top 10 imp features.png
```

---

# 🚀 Future Improvements

- Hyperparameter Tuning
- SHAP Explainability
- Model Monitoring
- Docker Containerization
- CI/CD Pipeline
- Cloud Deployment (AWS/GCP/Azure)

---

# ⭐ Project Outcome

Built an **end-to-end Machine Learning solution** capable of:

✔ Predicting customer churn with **77.86% accuracy**

✔ Generating actionable business insights

✔ Demonstrating the complete ML lifecycle:

**EDA → Preprocessing → Modeling → Evaluation → Business Analytics → Deployment**

---

# 👨‍💻 Author

## Apoorva Shree

📌 Aspiring Data Scientist & Machine Learning Engineer

🔗 GitHub: https://github.com/apoorva-shree

🔗 Live app : https://customer-churn-prediction-5ppqck2xqutudhe4chxaff.streamlit.app/

---

### ⭐ If you found this project interesting, consider giving it a star!
