from training import X,y, crop_s
import matplotlib.pyplot as plt
feature_names = X.columns  
feature_importances = crop_s.feature_importances_

plt.bar(range(len(feature_importances)), feature_importances, tick_label=feature_names)
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.title('Feature Importances in Random Forest Model')
plt.show()