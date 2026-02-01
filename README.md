# 🌬️ Weather-Based Prediction of Wind Turbine Energy Output

### A Next-Generation Approach to Renewable Energy Management

---

## 📌 Project Overview

This project focuses on **predicting the energy output of wind turbines based on weather conditions** using **Machine Learning and Flask**. Accurate energy prediction is crucial for renewable energy management, helping energy companies, wind farm operators, and grid operators make informed decisions.

By analyzing **historical wind and weather data**, a regression-based machine learning model is trained to predict turbine energy output under given weather conditions.

---

## 🎯 Problem Type

✔ **Regression Problem**
Because the output (energy in kWh) is a **continuous numerical value**, regression algorithms are used.

---

## 🌍 Real-World Scenarios

### 🔹 Scenario 1: Energy Production Forecasting

Energy companies can forecast wind turbine energy production using weather forecasts, enabling:

* Efficient energy distribution
* Dynamic pricing decisions
* Reduced energy wastage

### 🔹 Scenario 2: Maintenance Planning

Wind farm operators can:

* Predict low-wind periods
* Schedule maintenance to minimize downtime
* Maximize turbine availability during high-wind periods

### 🔹 Scenario 3: Grid Integration

Grid operators can:

* Balance renewable and conventional energy sources
* Adjust grid load dynamically
* Ensure stable and efficient energy supply

---

## 🏗️ Technical Architecture

**Workflow:**

1. User inputs weather-related data via UI
2. Flask backend processes the input
3. Machine learning model predicts energy output
4. Result is displayed on the web interface

---

## 🎯 Project Objectives

By completing this project, you will be able to:

* Identify whether a problem is **regression or classification**
* Perform **data preprocessing and cleaning**
* Visualize and analyze datasets for insights
* Apply suitable **machine learning algorithms**
* Train, test, and evaluate ML models
* Build a **Flask-based web application**
* Integrate ML models with a real-time UI

---

## 🔄 Project Flow

1. User interacts with the Web UI
2. Weather data is fetched (optional API integration)
3. Input is passed to the ML model
4. Model predicts wind turbine energy output
5. Prediction is displayed to the user

---

## 🧪 Project Phases

### 1️⃣ Data Collection

* Dataset collected from wind turbine historical records
* Stored in CSV format

### 2️⃣ Data Preprocessing

* Importing libraries
* Handling missing values
* Data cleaning and normalization
* Feature selection
* Train-test split

### 3️⃣ Data Visualization

* Wind speed vs power analysis
* Accuracy and performance graphs

### 4️⃣ Model Building

Regression algorithms used:

* Linear Regression
* Decision Tree Regression
* **Random Forest Regression** (final model)

### 5️⃣ Model Evaluation

* Accuracy comparison
* Performance analysis on test data

### 6️⃣ Application Building

* HTML + CSS frontend
* Flask backend
* Model integration using `joblib`

---

## 🛠️ Technologies Used

### 🧠 Machine Learning

* Python
* Scikit-learn
* NumPy
* Pandas
* Matplotlib

### 🌐 Web Development

* Flask
* HTML
* CSS
* JavaScript

---

## 📦 Prerequisites

### Software Requirements

* Anaconda Navigator
* Python 3.x
* Jupyter Notebook / Spyder
* Web Browser

### Required Python Packages

```bash
pip install numpy
pip install pandas
pip install matplotlib
pip install scikit-learn
pip install flask
pip install requests
```

---

## 📂 Project Structure

```text
Flask-Wind-Mill-Power-Prediction/
│
├── data/
│   └── T1.csv
│
├── static/
│   ├── style.css
│   ├── accuracy_graph.png
│   └── images/
│       ├── m123.gif
│       └── windmill.jpg
│
├── templates/
│   ├── intro.html
│   ├── predict.html
│   └── result.html
│
├── app.py
├── power_prediction.sav
├── train_model.py
├── test_model.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

### Step 1: Activate Environment

```bash
venv\Scripts\activate
```

### Step 2: Run Flask App

```bash
python app.py
```

### Step 3: Open Browser

```
http://127.0.0.1:5000/
```

---

## 🎨 Features

* 🌤 Weather-based energy prediction
* 🌙 Dark mode support
* ⏳ Loading animation
* 📊 Accuracy visualization
* ⚡ Real-time prediction output
* 📱 Responsive UI

---

## ✅ Conclusion

This project demonstrates how **machine learning and web technologies** can be combined to solve real-world renewable energy challenges. Predicting wind turbine energy output improves efficiency, planning, and grid stability, contributing to a more sustainable energy future.

---


## 👨‍💻 Developed By

**APSCHE AIML Project – Renewable Energy & Machine Learning**

- Aditya Indana