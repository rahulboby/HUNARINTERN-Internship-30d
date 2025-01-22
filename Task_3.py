import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# --- Importing file into dataframe
data = pd.read_csv(r"C:\Users\Rahul\Desktop\HunarIntern\Task 3\breast cancer.csv")

# --- Checking for missing values
print("Missing values per column: ", data.isnull().sum())
#found no missing values in the list

# --- Splitting into train and test data
y = data['diagnosis']
x = data.drop(columns=['diagnosis'])
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)

# --- Applying k-NN algorithm
knn_classifier = KNeighborsClassifier(n_neighbors=5) #choosing k as 5

knn_classifier.fit(train_x, train_y) # Training

prediction = knn_classifier.predict(test_x) # Testing

# --- Printing results of the model
accuracy = accuracy_score(test_y, prediction)
precision = precision_score(test_y, prediction, pos_label='M')
recall = recall_score(test_y, prediction, pos_label='M')
f1 = f1_score(test_y, prediction, pos_label='M')

print(f"Accuracy score: {accuracy:.2f}")
print(f"Precision score: {precision:.2f}")
print(f"recall score: {recall:.2f}")
print(f"F1 score: {f1:.2f}")

