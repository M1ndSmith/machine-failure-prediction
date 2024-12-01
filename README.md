# Machine Failure Prediction

This project is a Flask-based web application for predicting machine failures using a pre-trained Random Forest model. Users can input machine data through a web interface to receive failure predictions.

## Features

- Intuitive web interface for machine data input
- Machine failure prediction using a Random Forest machine learning model
- Interactive results page with prediction outcomes

## Dataset

**Note:** The dataset used for training is synthetic and generated using [Mockaroo](https://www.mockaroo.com/) for testing purposes only. It includes the following key features:

- `Operating_Hours`
- `Vibration_Level (mm/s)`
- `Maintenance_Overdue (days)`
- `Tool_Wear (mm)`
- `Ambient_Temperature (°C)`

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Setup and Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/M1ndSmith/machine-failure-prediction.git
cd machine-failure-prediction
```

### Step 2: Install Dependencies

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Generate the Machine Learning Model

If a pre-trained model is not included, generate the Random Forest model:

```bash
python rf_model.py
```

This will create the `rf_model.pkl` file used for predictions.

### Step 4: Run the Flask Application

Start the Flask development server:

```bash
python app.py
```

The application will be accessible at `http://localhost:5000`.

### Step 5: Use the Prediction Interface

1. Navigate to the web application in your browser
2. Input the machine data in the provided form
3. Click "Predict" to see the failure prediction result

## Project Structure

```
machine-failure-prediction/
├── MOCK_DATA.csv      # Dataset
├── app.py             # Main Flask application
├── rf_model.py     # Script to train the machine learning model
├── rf_model.pkl       # Serialized Random Forest model
├── requirements.txt   # Python dependencies
└── templates/         # HTML templates for the web interface
    └── index.html
    └── result.html
```

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page] (https://github.com/M1ndSmith/machine-failure-prediction/issues) if you want to contribute.



## Acknowledgments

- [Mockaroo](https://www.mockaroo.com/) for data generation
- [scikit-learn](https://scikit-learn.org/) for machine learning tools
- [Flask](https://flask.palletsprojects.com/) for web application framework
