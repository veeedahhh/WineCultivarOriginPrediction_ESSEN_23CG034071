# WineCultivarOriginPrediction_ESSEN_23CG034071

🍷 Wine Cultivar Origin Prediction System
📌 Project Overview

The Wine Cultivar Origin Prediction System is a machine learning web application designed to predict the cultivar (origin/class) of a wine sample based on its chemical properties.

The system uses the UCI / sklearn Wine Dataset, which contains chemical analysis results of wines derived from three different cultivars. A supervised machine learning model is trained and deployed using Streamlit to allow users to interactively input wine features and obtain predictions.

🎯 Objectives

Train a multiclass classification model to predict wine cultivars

Apply appropriate data preprocessing and feature scaling

Evaluate the model using standard classification metrics

Persist the trained model to disk

Build and deploy a user-friendly web interface using Streamlit

🧪 Dataset Information

Source: UCI Machine Learning Repository / sklearn Wine Dataset

Total Features: 13 numerical features

Target Variable: cultivar (3 classes: Cultivar 1, 2, 3)

Selected Input Features (6)

The following features were selected as inputs:

alcohol

malic_acid

alcalinity_of_ash

total_phenols

flavanoids

proline

🧠 Machine Learning Model

Algorithm Used: Support Vector Machine (SVM)

Kernel: Radial Basis Function (RBF)

Feature Scaling: StandardScaler

Model Persistence: Joblib

📊 Model Evaluation Metrics

The model was evaluated using multiclass classification metrics:

Accuracy

Precision (macro)

Recall (macro)

F1-score (macro)

Classification Report

🖥️ Web Application

Framework: Streamlit

Functionality:

Accepts user input for wine chemical properties

Scales input features

Predicts wine cultivar

Displays prediction as Cultivar 1, 2, or 3


🚀 Deployment

The application is deployed using Streamlit Cloud.


Live Application URL : [Click here[]](https://2eyqx2td29crmlyvkqpjz3.streamlit.app/)

GitHub Repository Link: [Click here[]](https://github.com/veeedahhh/WineCultivarOriginPrediction_ESSEN_23CG034071/)

✅ Technologies Used

Python

Scikit-learn

NumPy

Pandas

Joblib

Streamlit

📌 Author

Name: ESSEN DAVIDA TOROABASI
Matric Number: 23CG034071

