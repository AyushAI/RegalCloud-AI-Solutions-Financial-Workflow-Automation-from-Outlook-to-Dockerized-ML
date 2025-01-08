import pickle
from flask import Flask, render_template, request

# Load the pre-trained model
MODEL_PATH = "random_forest_model.pkl"
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('index.html')  # Input form

@app.route('/result', methods=['POST'])
def predict():
    # Retrieve form data
    input_data = request.form.get('input_data')  # Adjust 'input_data' based on your form field names
    
    # Convert input data to the format expected by the model (e.g., as a NumPy array or DataFrame)
    # Example: parsed_data = preprocess_function(input_data)  # Replace with actual preprocessing
    
    # Make prediction
    try:
        prediction = model.predict([[float(input_data)]])[0]  # Update based on input format
        prediction_text = "likely" if prediction == 1 else "unlikely"
    except Exception as e:
        prediction_text = f"Error: {e}"

    # Render the result
    return render_template('result.html', prediction=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
