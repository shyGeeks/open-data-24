#kutubxonlar importi
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

dataset_file_path = 'Crop_recommendation.xlsx'  # faylni o`qish
df = pd.read_excel(dataset_file_path)
# df.head()
