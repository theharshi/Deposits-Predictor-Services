import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import joblib
# from sklearn import joblib
import pandas as pd
# from xgboost import XGBRegressor
import pickle


app = Flask(__name__)
# model = joblib.load(open('deposits_model.pkl','rb'))
model = pickle.load(open('Model2.pkl', 'rb'))
# del data['Unnamed: 0']
data = pd.read_csv('complete_dataset_1.csv')

data.insert(0,'Gap',data['Inflation Rate'] - data['Interest Rate'])
# data['Gap'] = data['Inflation Rate'] - data['Interest Rate']
day = pd.DatetimeIndex(data['Date']).day
DATE = data['Date']
month = pd.DatetimeIndex(data['Date']).month
year = pd.DatetimeIndex(data['Date']).year
data.insert(0,'Day',day)
data.insert(0,'Year',year)
data.insert(0,'Month',month)
data.drop(range(0,20), inplace = True )
data.reset_index(drop=True, inplace=True)
# data['Month'] = data.index.day
# data['Year'] = data.index.year
print(len(data))
data['date'] = DATE
del data['Date']

print(data.head())
@app.route('/')
def home():
    return 'Hello World'
    # return render_template('home.html')
    #return render_template('index.html')

@app.route('/api/predict/<int:count>',methods = ['GET'])
def predict(count):
    # return "count is " + count
    # x = current_row

    x_train = data.iloc[0:count,0:7]

    prediction = model.predict(x_train)
    prediction = prediction.tolist()
    # print(prediction.shape)
    # output =prediction
    #output = round(prediction[0], 2)
    return jsonify({" predictions " : prediction })


@app.route('/api/predict_date/<type>/<fromDate>/<toDate>', methods=['GET'])
def predict_date(type,fromDate,toDate):
    # return "count is " + count
    # x = current_row
    idx = 0
    st = 0
    en = 0
    for i in range(len(data)):
        if data.iloc[i, 10] == fromDate :
            st = i
            break
    for i in range(len(data)):
        if data.iloc[i, 10] == toDate :
            en = i
            break
    count = en - st
    idx = st
    print("count ",count)
    print("st en ",st, " ",en)
    X = data.iloc[idx:idx + count, 10]
    X = X.tolist()
    x_train = data.iloc[idx:idx + count, 0:8]
    prediction = model.predict(x_train)
    prediction = prediction.tolist()
    # print(prediction.shape)
    # output =prediction
    # output = round(prediction[0], 2)
    return jsonify({"Y": prediction,"X":X})

@app.route('/api/predict2/', methods=['GET'])
def predict2():
    # return "count is " + count
    # x = current_row
    params = request.args.to_dict()
    print(params)
    type = params["type"]
    from_year = params["fyear"]
    from_month = params["fmonth"]
    to_year = params["tyear"]
    to_month = params["tmonth"]
    st = 0
    en = 0
    for i in range(len(data)):
        if data.iloc[i, 0] == from_year and data.iloc[i, 1] == from_month:
            st = i
            break
    for i in range(len(data)):
        if data.iloc[i, 0] == to_year and data.iloc[i, 1] == to_month:
            en = i
            break
    idx = st
    count = en - st
    x_train = data.iloc[idx:idx + count, 0:7]
    prediction = model.predict(x_train)
    prediction = prediction.tolist()
    # print(prediction.shape)
    # output =prediction
    # output = round(prediction[0], 2)
    return jsonify({"Deposits ": prediction})




if __name__ == '__main__':
    app.run(debug=True)