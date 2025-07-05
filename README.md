career-path-recommender
💼 Career Path Recommender System
This project uses a Decision Tree Classifier to predict the most suitable career path based on a student's skill ratings in five key areas:

Math
Science
Communication
Creativity
Logical Thinking
It is designed as a beginner-friendly machine learning project for educational purposes.

🧠 Objective
To recommend career options like Engineer, Data Scientist, HR, or Marketing based on input skill scores using a supervised machine learning algorithm.

🔧 Technologies Used
Python
pandas – for data manipulation
scikit-learn – for model training and evaluation
📁 Dataset
A manually created dataset with 8–10 samples where each row represents skill scores and the corresponding career label.

Math	Science	Communication	Creativity	Logical	Career
9	8	4	5	9	Engineer
4	2	9	10	3	Marketing
6	5	6	6	7	Data Scientist
...	...	...	...	...	...
🛠️ How It Works
The dataset is loaded using pandas.
Features (X) and target (y) are separated.
Data is split into training and testing sets using train_test_split.
A DecisionTreeClassifier is trained on the training data.
Model predictions are compared with the test set using accuracy_score.
📈 Sample Output
Accuracy: 0.75
Suggested Career Path: Data Scientist
