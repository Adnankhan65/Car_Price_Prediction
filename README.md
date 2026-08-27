# 🚗 Car Price Prediction

A Machine Learning web application that predicts the estimated price of a used car based on its **company, car model, manufacturing year, kilometers driven, and fuel type**.

This project covers the complete Machine Learning workflow — from **raw data cleaning and exploratory data analysis to model development and deployment using Streamlit**.

---

## 🌐 Live Demo

🚀 **Try the deployed application:**
https://adnankhan-carpriceprediction.streamlit.app/

---

## 📌 Project Overview

Buying or selling a used car can be challenging because the price depends on several factors such as brand, model, age, mileage, and fuel type.

The goal of this project is to build a Machine Learning model that estimates the price of a used car based on these features.

The original dataset was scraped from **Quikr.com** and required significant data cleaning and preprocessing before it could be used for analysis and Machine Learning.

After cleaning and analyzing the dataset, a **Linear Regression model** was developed and achieved an **R² score of 0.92** on the evaluation data.

The trained model was then integrated into a **Streamlit web application**, allowing users to enter car details and receive an estimated price instantly.

---

## 🎯 Objectives

* Collect used-car data from Quikr.com
* Clean and preprocess the raw dataset
* Perform Exploratory Data Analysis (EDA)
* Understand factors affecting car prices
* Prepare the data for Machine Learning
* Train a Linear Regression model
* Evaluate model performance
* Deploy the model using Streamlit
* Build an interactive prediction interface

---

## 📊 Dataset

The dataset was scraped from **Quikr.com** and contains information about used cars.

### Main Features

| Feature      | Description                           |
| ------------ | ------------------------------------- |
| `name`       | Name/model of the car                 |
| `company`    | Car manufacturer/brand                |
| `year`       | Manufacturing year                    |
| `kms_driven` | Kilometers driven                     |
| `fuel_type`  | Type of fuel used                     |
| `Price`      | Target variable — estimated car price |

### Raw Dataset

The original scraped dataset is available in:

`quikr_car.csv`

### Cleaned Dataset

After preprocessing, the cleaned dataset is available in:

`Cleaned_Car_data.csv`

---

## 🧹 Data Cleaning & Preprocessing

The raw dataset required substantial cleaning before Machine Learning could be performed.

The preprocessing workflow included:

* Handling missing values
* Removing invalid records
* Removing unnecessary columns
* Cleaning inconsistent text values
* Converting numerical features into appropriate data types
* Handling inconsistent values in price and kilometers driven
* Removing duplicate/unusable records
* Preparing categorical variables for Machine Learning

Data cleaning was an important step because the original scraped dataset contained inconsistent and unusable records.

---

## 🔎 Exploratory Data Analysis

EDA was performed to understand the relationship between car characteristics and their prices.

The analysis focused on:

* Car companies and their price ranges
* Relationship between car age and price
* Effect of kilometers driven on price
* Fuel type distribution
* Popular car models
* Distribution of car prices
* Identification of unusual or inconsistent records

The analysis helped understand the dataset before building the predictive model.

---

## 🤖 Machine Learning Model

### Linear Regression

A **Linear Regression** model was trained to estimate the price of a used car.

The model uses the following input features:

```text
Car Model
Company
Year
Kilometers Driven
Fuel Type
```

Categorical features were processed before being passed to the model.

---

## 📈 Model Performance

### **R² Score: 0.92**

The Linear Regression model achieved an **R² score of 0.92** on the evaluation data.

This means the model explains approximately **92% of the variance in the target variable on the evaluation data**.

> Note: R² is not the same as prediction accuracy. It measures how well the model explains variation in the target variable.

---



## 🌐 Streamlit Application

The trained Machine Learning model was integrated into an interactive Streamlit application.

Users can select:

* Company
* Car Model
* Manufacturing Year
* Fuel Type
* Kilometers Driven

After clicking **"Predict Car Price"**, the application returns the estimated price.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* Linear Regression

### Data Visualization

* Matplotlib
* Seaborn

### Deployment

* Streamlit

### Development Tools

* Jupyter Notebook
* GitHub

---

## 📁 Project Structure

```text
Car-Price-Prediction/
│
├── Car Analysis.ipynb
├── Cleaned_Car_data.csv
├── LinearRegressionModel.pkl
├── quikr_car.csv
├── app.py
├── requirements.txt
└── README.md
```



## 👨‍💻 Author

### Mohammed Adnan Khan

Aspiring Data Analyst with an interest in **Data Analytics, Machine Learning, Python, SQL, and Business Intelligence**.

**GitHub:**
https://github.com/Adnankhan65



---

## ⭐ If you found this project useful

Feel free to ⭐ star the repository and explore the project.

