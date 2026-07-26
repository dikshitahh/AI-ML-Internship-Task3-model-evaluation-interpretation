# Model Evaluation and Interpretation Report

## Introduction

The objective of this project was to evaluate the performance of a Random Forest Classifier for predicting heart disease and to interpret its predictions using SHAP.

## Data Preprocessing

The dataset was loaded using Pandas and examined for missing values and duplicate records.

- Missing Values: None
- Duplicate Records: Removed if present

The features and target variable were separated before splitting the data into training and testing sets.

## Model Training

A Random Forest Classifier was trained using the training dataset.

Model Parameters:

- Algorithm: Random Forest Classifier
- Number of Trees: 100
- Random State: 42

## Performance Evaluation

The model was evaluated using multiple classification metrics.

### Accuracy

Accuracy measures the percentage of correctly classified instances.

### Precision

Precision indicates how many predicted positive cases were actually positive.

### Recall

Recall measures the model's ability to correctly identify patients with heart disease.

### F1-score

The F1-score balances precision and recall into a single performance metric.

### Confusion Matrix

The confusion matrix summarizes correct and incorrect predictions by displaying:

- True Positives
- True Negatives
- False Positives
- False Negatives

### ROC Curve

The Receiver Operating Characteristic (ROC) Curve illustrates the model's ability to distinguish between the two classes across different classification thresholds.

### Area Under the Curve (AUC)

AUC provides an overall measure of classification performance independent of a specific threshold. A value closer to 1 indicates excellent discrimination.

## SHAP Interpretation

SHAP (SHapley Additive exPlanations) was used to explain the predictions of the Random Forest model.

### Global Interpretation

The SHAP Beeswarm Plot identified the most influential features affecting model predictions across the entire dataset.

Highly influential features included:

- Chest Pain Type (cp)
- Number of Major Vessels (ca)
- ST Depression (oldpeak)
- Maximum Heart Rate (thalach)
- Age

### Local Interpretation

The SHAP Waterfall Plot explained the prediction for an individual patient by illustrating how each feature increased or decreased the predicted probability of heart disease.

## Conclusion

The Random Forest model demonstrated strong predictive performance for heart disease classification. Evaluation metrics confirmed good classification capability, while SHAP improved model transparency by explaining the contribution of each feature. Such interpretability is particularly valuable in healthcare applications, where understanding the reasoning behind predictions is essential for building trust in machine learning models.

