import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv("career_dataset.csv")
X = df.drop('Career', axis=1)
y = df['Career']
model = DecisionTreeClassifier()
model.fit(X, y)
st.title("🎓 Career Path Recommender System")
math = st.slider("Math Skill", 1, 10, 5)
science = st.slider("Science Skill", 1, 10, 5)
comm = st.slider("Communication Skill", 1, 10, 5)
creativity = st.slider("Creativity", 1, 10, 5)
logical = st.slider("Logical Thinking", 1, 10, 5)
if st.button("Predict Career"):
    user_input = pd.DataFrame([[math, science, comm, creativity, logical]],
                              columns=X.columns)
    prediction = model.predict(user_input)
    st.success(f"✅ Suggested Career Path: {prediction[0]}")
