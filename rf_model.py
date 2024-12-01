import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load your data (replace 'MOCK_DATA.csv' with your dataset file)
file_path = "MOCK_DATA.csv""
data = pd.read_csv(file_path)

# List of top features to use
top_features = [
    'Operating_Hours',
    'Vibration_Level (mm/s)',
    'Maintenance_Overdue (days)',
    'Tool_Wear (mm)',
    'Ambient_Temperature (°C)'
]

# Ensure the data contains the specified features
if not all(feature in data.columns for feature in top_features):
    raise ValueError("Some of the specified top_features are missing from the dataset.")

# Prepare the data
X = data[top_features]  # Use only the top features
y = data['Failure']  # Target variable

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, shuffle=False)

# Train the Random Forest model
rf_model = RandomForestClassifier(random_state=42, min_samples_leaf=1, min_samples_split=5, n_estimators=200)
rf_model.fit(X_train, y_train)

# Save the model
save_path = 'rf_model.pkl'
with open(save_path, 'wb') as file:
    pickle.dump(rf_model, file)

print(f"Model saved as '{save_path}'.")
