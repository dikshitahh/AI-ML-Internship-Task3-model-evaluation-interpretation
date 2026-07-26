# AI-ML-Internship-Task3-model-evaluation-interpretation

# Heart Disease Prediction: Model Evaluation and Interpretation

## Project Overview

This project demonstrates the evaluation and interpretation of a machine learning classification model using the Heart Disease dataset. A Random Forest Classifier was trained to predict whether a patient has heart disease based on various clinical features.

The project focuses not only on prediction accuracy but also on understanding model behavior through explainable AI techniques such as SHAP (SHapley Additive exPlanations).

## Objectives

- Train a Random Forest classification model.
- Evaluate model performance using multiple evaluation metrics.
- Generate a Confusion Matrix.
- Plot the ROC Curve and calculate the AUC score.
- Interpret model predictions using SHAP.
- Analyze feature importance using both Random Forest and SHAP.

## Dataset

The dataset contains patient health information including:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression (Oldpeak)
- Slope
- Number of Major Vessels (ca)
- Thalassemia (thal)

Target Variable:

- 0 → No Heart Disease
- 1 → Heart Disease

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SHAP

## Project Workflow

1. Import libraries
2. Load dataset
3. Explore dataset
4. Check missing values
5. Check duplicate values
6. Split features and target
7. Train-test split
8. Feature scaling
9. Train Random Forest model
10. Make predictions
11. Evaluate model performance
12. Generate Confusion Matrix
13. Plot ROC Curve
14. Calculate AUC Score
15. Interpret model using SHAP
16. Analyze feature importance

## Evaluation Metrics

The following metrics were used:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC Curve
- Area Under Curve (AUC)

## Explainable AI

SHAP was used to explain the predictions made by the Random Forest model.

The project includes:

- SHAP Beeswarm Plot (Global Interpretation)
- SHAP Waterfall Plot (Local Interpretation)

These visualizations help understand how each feature contributes to the prediction.

## Conclusion

The Random Forest model achieved strong classification performance on the Heart Disease dataset. Model evaluation metrics demonstrated reliable predictive capability, while SHAP provided valuable insights into the contribution of individual features. This combination of predictive performance and interpretability makes the model more transparent and trustworthy for healthcare-related applications.
