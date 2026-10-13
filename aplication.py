from flask import Flask ,render_template, request
import pandas as pd
import numpy as np

model = pd.read_pickle('LinearRegressionmodel (1).pkl')
app = Flask(__name__)

car = pd.read_csv('clend_data (3).csv')

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(),reverse=True)
    fuel_types = sorted(car['fuel_type'].dropna().unique())

    return render_template('index.html',companies=companies,car_models=car_models,year=year,fuel_type=fuel_types)
   
@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    kms_driven = int(request.form.get('kms_driven'))
    fuel_type = request.form.get('fuel_type')

    # Model train korar somoy columns je order e chilo, ekhane o thik rakhte hobe
    input_data = pd.DataFrame(
        [[car_model, company, year, kms_driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )

    prediction = model.predict(input_data)
   
   
    return f"Predicted Price: ₹{np.round(prediction[0], 2)}"



if __name__ == '__main__':
    app.run(debug = True)