# # Load the pre-trained model
# MODEL_PATH = "random_forest_model.pkl"
# with open(MODEL_PATH, "rb") as f:
#     model = pickle.load(f)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def predict():
    prediction = "unlikely"
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
