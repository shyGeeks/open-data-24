from training import crop_s, X_test, y_test
from sklearn.metrics import accuracy_score, classification_report

#modelni baholash 
y_pred = crop_s.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
