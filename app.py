# -*- coding: utf-8 -*-
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

def get_predictions(V2, V4, V11, Amount):
    mylist = [V2, V4, V11, Amount]
    mylist = [float(i) for i in mylist]
    vals = [mylist]
    return model.predict(vals)[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def predict():
       if request.method == 'POST':
        V2 = request.form['V2']
        V4 = request.form['V4']
        V11 = request.form['V11']
        Amount = request.form['Amount']
       
        target = get_predictions(V2, V4, V11, Amount)

        if target==1:
            sale_making = 'Fraud detected'
        else:
            sale_making = 'No Fraud detected'

        return render_template('index.html', target = target, sale_making = sale_making)
     

        

if __name__ == "__main__":
   app.run(debug=True)