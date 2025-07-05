# 🎓 Career Path Recommender System

A simple machine learning project that suggests a suitable career path based on a user's skills in Math, Science, Communication, Creativity, and Logical Thinking. Built using **Python**, **scikit-learn**, **pandas**, and **Streamlit**.

---

## 🧠 Project Overview

This application uses a **Decision Tree Classifier** to predict career options like:

- Engineer  
- Data Scientist  
- Marketing  
- HR

The user provides their skill ratings (1 to 10) through an interactive UI created using Streamlit, and the model suggests the best-fit career path.

---

## 🛠️ Technologies Used

- Python
- pandas
- scikit-learn
- Streamlit

---

## 📁 Dataset

A small manually created dataset stored as `career_dataset.csv`, with the following columns:

| Math | Science | Communication | Creativity | Logical | Career         |
|------|---------|----------------|------------|---------|----------------|
| 9    | 8       | 4              | 5          | 9       | Engineer       |
| 4    | 2       | 9              | 10         | 3       | Marketing      |
| 6    | 5       | 6              | 6          | 7       | Data Scientist |
| ...  | ...     | ...            | ...        | ...     | ...            |

---

## 🚀 How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/career-path-recommender.git
cd career-path-recommender
