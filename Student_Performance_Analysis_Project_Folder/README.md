# Student Performance Analysis

## Overview

This project performs Exploratory Data Analysis (EDA) on a student performance dataset using Python, Pandas, NumPy, and Matplotlib.

The analysis focuses on understanding student performance and exploring relationships between final grades and factors such as study
time, previous failures, absences, school, gender, and other student-related attributes.

## Objectives

The main objectives of this project are:

- Understand the structure of the student performance dataset.
- Analyze the distribution of final grades.
- Study the relationship between study time and final grades.
- Analyze the effect of previous failures and absences on student performance.
- Compare performance across different student groups.
- Analyze the relationship between G1, G2, and G3 grades.
- Perform data quality checks.
- Create visualizations to identify patterns in the data.

## Dataset

The dataset contains **395 student records and 33 columns**.

Some important columns include:

- `school` – Student's school
- `sex` – Student's gender
- `age` – Student's age
- `studytime` – Weekly study time
- `failures` – Number of past class failures
- `absences` – Number of school absences
- `G1` – First period grade
- `G2` – Second period grade
- `G3` – Final grade

The analysis uses `G3` as the main indicator of final student performance.

## Data Quality Check

The project checks:

- Missing values
- Duplicate records
- Data types
- Unique values
- Basic statistical information

The dataset contains **no missing values** and **no duplicate records** according to the checks performed in the notebook.

## Analysis Performed

### 1. Dataset Overview

- Dataset dimensions
- Column names
- Data types
- Descriptive statistics

### 2. Data Quality Check

- Missing value analysis
- Duplicate value analysis
- Data type verification
- Unique value analysis

### 3. Exploratory Data Analysis

- Distribution of final grades
- Average final grade
- Minimum and maximum final grades
- Median final grade
- Study time vs final grade
- Previous failures vs performance
- Absences vs performance
- School-wise performance
- Gender-wise performance

### 4. Correlation Analysis

The project also explores the relationship between:

- G1 and G3
- G2 and G3
- G1 and G2

## Key Results

Based on the analysis:

- Total students: **395**
- Total columns: **33**
- Average final grade (G3): **10.42**
- Median final grade (G3): **11**
- Minimum final grade (G3): **0**
- Maximum final grade (G3): **20**
- Average absences: **5.71**

The analysis also shows that students with different levels of study time have different average final grades, and the project explores
how previous failures and absences relate to final performance.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Project Structure

```text
Student-Performance-Analysis/
│
├── Student_Performance_Analysis.ipynb
├── README.md
├── requirements.txt
└── LICENSE
