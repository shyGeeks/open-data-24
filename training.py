#kutubxonlar importi
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

dataset_file_path = 'Crop_recommendation.xlsx'  # faylni o`qish
df = pd.read_excel(dataset_file_path)
# df.head()


X = df.iloc[:, :-1]  # Features
y = df.iloc[:, -1]   # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# modelni baholash 
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy}")

new_data = [[12, 50, 46, 19.770462, 230.319644, 7.038096, 150.655537]]
prediction = model.predict(new_data)
print(prediction)