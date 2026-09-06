# Student Performance Analysis

## Overview

This project performs Exploratory Data Analysis (EDA) on a student performance dataset using Python, Pandas, NumPy, and Matplotlib.

The main purpose of this project is to understand student academic performance and explore how different factors are related to students' final grades.

## Dataset

The dataset contains:

- 395 student records
- 33 columns

The analysis mainly focuses on the final grade (`G3`) and its relationship with different student and academic attributes.

Some important columns used in the analysis include:

- `school` – Student's school
- `sex` – Student's gender
- `age` – Student's age
- `studytime` – Weekly study time
- `failures` – Number of previous class failures
- `absences` – Number of school absences
- `G1` – First period grade
- `G2` – Second period grade
- `G3` – Final grade

## Objectives

The main objectives of this project are:

- Understand the structure of the dataset.
- Check the quality of the data.
- Analyze the distribution of final grades.
- Calculate important statistics for final grades.
- Analyze the relationship between study time and final grades.
- Analyze the relationship between previous failures and final grades.
- Explore the relationship between absences and student performance.
- Compare average performance across schools.
- Compare average performance by gender.
- Analyze the correlation between G1, G2, and G3.
- Create visualizations to understand patterns in the data.

## Data Quality Check

The project includes checks for:

- Missing values
- Duplicate records
- Data types
- Unique values
- Basic statistical information

The dataset was checked for missing values and duplicate records during the analysis.

## Exploratory Data Analysis

The following analyses were performed:

### Final Grade Analysis

The final grade (`G3`) was analyzed using:

- Mean
- Median
- Minimum value
- Maximum value
- Grade distribution

### Study Time Analysis

The project explores how different levels of weekly study time are related to students' final grades.

### Previous Failures Analysis

The relationship between the number of previous failures and final academic performance was explored.

### Absence Analysis

The project analyzes students' absences and explores their relationship with final grades.

### School-wise Analysis

Average final grades were compared between different schools.

### Gender-wise Analysis

Average final grades were also compared across genders.

## Correlation Analysis

The project analyzes the relationship between:

- `G1` and `G3`
- `G2` and `G3`
- `G1` and `G2`

This helps understand how earlier grades are related to the final grade.

## Key Statistics

From the dataset analysis:

- **Total Students:** 395
- **Total Columns:** 33
- **Average Final Grade (G3):** 10.42
- **Median Final Grade (G3):** 11
- **Highest Final Grade (G3):** 20
- **Lowest Final Grade (G3):** 0
- **Average Absences:** 5.71

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Project Structure

```text
Student_Performance_Analysis_Project_Folder/
│
├── Student_Performance_Analysis.ipynb
├── student-mat.csv
├── README.md
└── requirements.txt
