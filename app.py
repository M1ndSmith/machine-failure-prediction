from flask import Flask, request, render_template
import numpy as np
import pickle

# Initialize the Flask app
app = Flask(__name__)

# Load the trained Random Forest model
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the top features (ensure this matches the training data)
top_features = [
    'Operating_Hours',
    'Vibration_Level (mm/s)',
    'Maintenance_Overdue (days)',
    'Tool_Wear (mm)',
    'Ambient_Temperature (°C)'
]

# Define the homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Define the predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect inputs from the form
        input_data = []
        for feature in top_features:
            input_value = request.form.get(feature)
            if input_value is None or not input_value.strip():
                return f"Missing input for {feature}. Please fill all fields."
            try:
                input_value = float(input_value)
            except ValueError:
                return f"Invalid input for {feature}. Please enter a valid number."
            input_data.append(input_value)

        # Prepare the data for prediction
        input_array = np.array(input_data).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_array)[0]
        result = "Failure" if prediction else "No Failure"

        return render_template('result.html', prediction=result)

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
