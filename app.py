import pickle
from flask import Flask, render_template, request

# Load the pre-trained model
MODEL_PATH = "random_forest_model.pkl"
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

# Preprocess function
def preprocess_function(input_data):
    """
    Preprocesses the input data from the form.
    Converts a comma-separated string of numbers into a list of floats.
    
    :param input_data: str - Comma-separated input from the form
    :return: list - List of floats
    """
    try:
        # Split the input by commas, strip whitespace, and convert to floats
        processed_data = [float(value.strip()) for value in input_data.split(',')]
        return processed_data
    except ValueError as e:
        raise ValueError(f"Invalid input format: {e}. Please enter numerical values separated by commas.")

# Define routes
@app.route('/')
def home():
    return render_template('index.html')  # Input form

@app.route('/result', methods=['POST'])
def predict():
    # Retrieve form data
    input_data = request.form.get('input_data')  # Adjust 'input_data' based on your form field names
    
    try:
        # Preprocess input data
        parsed_data = preprocess_function(input_data)
        
        # Make prediction
        prediction = model.predict([parsed_data])[0]  # Assuming the model takes a single feature vector
        prediction_text = "likely" if prediction == 1 else "unlikely"
    except Exception as e:
        prediction_text = f"Error: {e}"

    # Render the result
    return render_template('result.html', prediction=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
