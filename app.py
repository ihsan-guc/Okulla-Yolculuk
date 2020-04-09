#import the libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#flask configuration
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#route configurations
@app.route("/")
def home():
    return render_template("index.html")

#prediction route
@app.route("/predict", methods = ['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    predictionValue = str(prediction)
    print(str(prediction))
    if str(prediction) == "[[0. 0. 1.]]":
        output = "Yürüyerek ";
    if str(prediction) == "[[0. 1. 0.]]":
        output = "Bisiklet ile";    
    if str(prediction) == "[[1. 0. 0.]]":
        output = "Araba ile ";
    return render_template("index2.html", prediction_text = "Girdiğiniz verilere göre  {} Gidersiniz".format(output));

#run the app
if __name__ == "__main__":
    app.run(debug = True)