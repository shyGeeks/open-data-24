from training import crop_s 

#modelni baholash 
y_pred = crop_s.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
