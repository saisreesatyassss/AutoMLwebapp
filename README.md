# AutoML Web App

## Overview

AutoML Web App is a user-friendly application designed to streamline data analysis and machine learning workflows. Whether you're a data enthusiast or a seasoned data scientist, this app simplifies the process of uploading, profiling, and modeling, providing valuable insights with just a few clicks.

## Features

### 1. Upload Data
- Easily upload CSV files for analysis.
![image](https://github.com/saisreesatyassss/AutoMLwebapp/assets/132558766/9fee61ea-4b43-42fa-b1ad-a10cc9022ea7)

### 2. Automated Profiling
- Utilizes `streamlit_pandas_profiling` to generate Pandas Profiling reports for quick data exploration.
![image](https://github.com/saisreesatyassss/AutoMLwebapp/assets/132558766/a929efcf-e035-43b2-aae8-9a2a6c01ea57)

### 3. Machine Learning Models
- Leverages PyCaret for effortless setup, model building, and comparison.
- Handles class imbalances, ensuring robust model performance.
![image](https://github.com/saisreesatyassss/AutoMLwebapp/assets/132558766/5f043072-5b99-436f-a6e6-9ba292a0778a)

### 4. Model Download
- Save your best-trained model for future predictions.
- Download the model in the `.pkl` format for seamless integration.
![image](https://github.com/saisreesatyassss/AutoMLwebapp/assets/132558766/db4784de-32a1-47bb-a1db-46aa16e41bc6)

## Under the Hood

### Libraries Used
- **Streamlit:** Creates the interactive web application.
- **Pandas:** Handles data manipulation and analysis.
- **PyCaret:** Simplifies the machine learning workflow.

### Profiling
- Integrates `streamlit_pandas_profiling` to generate informative Pandas Profiling reports.
- Provides a comprehensive overview of data characteristics.

### Modeling
- Utilizes PyCaret for setting up the data, building models, and comparing their performance.
- Implements strategies to handle class imbalances for more accurate predictions.

### Deployment
- Suitable for deployment on platforms like Streamlit Sharing.
- The app provides an accessible interface for users to experience data analysis and modeling.

## Code Structure

- **app.py:** Contains the main Streamlit application code.
- **requirements.txt:** Lists all the dependencies for easy installation.

## Explore the Code

The code is open-source and available on [GitHub](<https://github.com/saisreesatyassss/AutoMLwebapp>). Feel free to explore, contribute, or customize it based on your requirements.

## Live Demo

Experience the AutoML Web App live [here](<https://automlwebapp1.streamlit.app/>) and witness the power of automated data analysis and machine learning model building.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/saisreesatyassss/AutoMLwebapp
