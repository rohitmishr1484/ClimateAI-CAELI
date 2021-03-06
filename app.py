from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import os
import glob
import predict_class_label

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_html():
    return render_template('index.html')

@app.route('/about/',methods=['GET'])
def about_html():
    return render_template('about.html')

@app.route('/usecase/', methods=['GET'])
def usecase_html():
    return render_template('usecase.html')

@app.route('/eda/', methods=['GET'])
def eda_html():
    return render_template('eda.html')

@app.route('/demo/', methods=['GET', 'POST'])
def demo_html():
    if request.method == 'POST':
        image_file = request.files["image"]
        
        if image_file:

            __prediction , __prediction_prob = predict_class_label.prediction(test_image_path = image_file)
            return render_template('demo.html', _prediction = __prediction,\
                 _prediction_prob = __prediction_prob)
    return render_template('demo.html', _prediction = 'NA', _prediction_prob= 0.0)

if __name__=="__main__":
    app.run(debug=True)