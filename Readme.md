\# Drug Classification Using Machine Learning



\## Project Overview



This project uses Machine Learning techniques to predict the most suitable drug for a patient based on medical attributes such as Age, Sex, Blood Pressure (BP), Cholesterol level, and Sodium-to-Potassium ratio (Na\_to\_K).



The project includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, visualization, and a user prediction system.



\---



\## Dataset



The dataset used is \*\*Drug200\*\*, which contains patient information and the corresponding drug prescribed.



\### Features



| Feature | Description |

|----------|------------|

| Age | Patient Age |

| Sex | Male (M) or Female (F) |

| BP | Blood Pressure (HIGH, NORMAL, LOW) |

| Cholesterol | Cholesterol Level (HIGH, NORMAL) |

| Na\_to\_K | Sodium to Potassium Ratio |

| Drug | Target Variable |



\---



\## Technologies Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Scikit-Learn



\---



\## Exploratory Data Analysis (EDA)



The following analyses were performed:



\- Dataset Overview

\- Missing Value Check

\- Statistical Summary

\- Drug Distribution Analysis

\- Age Distribution

\- Blood Pressure Distribution

\- Cholesterol Distribution

\- Correlation Analysis

\- Feature Visualization



\---



\## Data Preprocessing



The following preprocessing steps were applied:



\- Label Encoding for categorical features

\- Feature Selection

\- Train-Test Split

\- Feature Scaling (for KNN)

\- Target Encoding



\---



\## Machine Learning Models



\### 1. Logistic Regression



Logistic Regression was trained and evaluated using the processed dataset.



\### 2. K-Nearest Neighbors (KNN)



KNN was trained after applying feature scaling to ensure distance-based calculations perform correctly.



\---



\## Model Evaluation



The models were evaluated using:



\- Accuracy Score

\- Precision Score

\- Recall Score

\- F1 Score

\- Confusion Matrix



\---



\## User Prediction System



The project includes an interactive prediction system where users can enter:



\- Age

\- Sex

\- Blood Pressure

\- Cholesterol Level

\- Na\_to\_K Ratio



The trained model predicts the most suitable drug based on the provided information.



Example:



```text

Enter Age: 45

Enter Sex (M/F): M

Enter BP (HIGH/NORMAL/LOW): HIGH

Enter Cholesterol (HIGH/NORMAL): HIGH

Enter Na\_to\_K: 15.5



Predicted Drug: drugY

```



\---



\## Project Structure



```text

Drug-Classifier/

│

├── DRUG\_CLASSIFIER.ipynb

├── drug200.csv

├── README.md

├── requirements.txt

└── images/

```



\---



\## Installation



Clone the repository:



```bash

git clone https://github.com/your-username/Drug-Classifier.git

```



Move into the project directory:



```bash

cd Drug-Classifier

```



Install dependencies:



```bash

pip install -r requirements.txt

```



Run the notebook:



```bash

jupyter notebook

```



\---



\## Results



The models achieved high classification accuracy on the Drug200 dataset.



Logistic Regression and KNN both performed effectively for predicting drug categories based on patient medical information.



\---



\## Future Improvements



\- Hyperparameter Tuning

\- Cross Validation

\- Additional Machine Learning Models

\- Web-Based Prediction Interface

\- Model Deployment using Flask or FastAPI



\---



\## Author



Developed as a Machine Learning classification project for educational and learning purposes.

