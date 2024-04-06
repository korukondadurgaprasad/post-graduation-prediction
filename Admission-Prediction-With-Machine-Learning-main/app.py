import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("C:\\Users\\prasa\\Downloads\\Admission-Prediction-With-Machine-Learning-main\\Admission-Prediction-With-Machine-Learning-main\\model.pkl", "rb"))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods = ["POST"])
def predict():
    
    int_scores = [float(x) for x in request.form.values()]
    scores = [np.array(int_scores)]
    prediction = model.predict(scores)
    
    output = 100 * prediction[0]
    
    return render_template('index.html', prediction_text = "Percent of Admission is %{}".format(output))

if __name__ == "__main__":
    app.run(debug=True)