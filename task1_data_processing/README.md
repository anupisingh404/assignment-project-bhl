# 📊 Task 1 - Data Preprocessing & Feature Engineering

This notebook focuses on cleaning, preprocessing, and feature engineering using a realistic dataset (`sample_dataset.csv`) as part of a backend assessment assignment.

---

## 🗂️ Contents

- Load and inspect dataset
- Identify and handle missing values
- Feature engineering
- Data optimization (memory)
- Save cleaned dataset

---

## 📁 Files

| File                 | Description                                       |
|----------------------|---------------------------------------------------|
| `sample_dataset.csv` | Raw input data with missing values                |
| `processed_data.csv` | Cleaned & feature-enhanced output                 |
| `preprocessing.ipynb`| Step-by-step notebook for data preparation        |

---

## 🧪 Dataset Overview

- 100 rows
- Columns include:
  - `id`, `name`, `age`, `salary`, `department`
  - `join_date`, `last_active` (dates with some missing)

---

## 🧹 Data Cleaning Steps

1. **Load the dataset**  
   Read the CSV into a pandas DataFrame.

2. **Missing value analysis**  
   Identify columns with `NaN` and their percentage.

3. **Imputation strategy**  
   Used **forward fill (`ffill`)** for simplicity in this synthetic example.

4. **Feature engineering**  
   Extracted `day_of_week_joined` from the `join_date`.

5. **Memory optimization**  
   Used `pd.to_numeric(..., downcast='float')` to reduce memory usage.

---

## 💾 Output

The final cleaned dataset was saved to:

```bash
processed_data.csv
