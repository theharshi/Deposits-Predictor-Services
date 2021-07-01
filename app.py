import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
from data import *
import joblib
# from sklearn import joblib
import pandas as pd
# from xgboost import XGBRegressor
import pickle
Models = ['./models/Model_deposits.pkl','./models/Model_withdrawal.pkl']

app = Flask(__name__)

data = create_data()
@app.route('/')
def home():
    return 'Hello World'
@app.route('/api/predict/<int:type>/<int:count>',methods = ['GET'])
def predict(count):
    x_train = data.iloc[0:count,0:8]
    model = pickle.load(open(Models[type], 'rb'))
    prediction = model.predict(x_train)
    prediction = prediction.tolist()
    return jsonify({" predictions " : prediction })


@app.route('/api/predict_date/<int:type>/<fromDate>/<toDate>', methods=['GET'])
def predict_date(type,fromDate,toDate):
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
    model = pickle.load(open(Models[type], 'rb'))
    print("count ",count)
    print("st en ",st, " ",en)
    X = data.iloc[idx:idx + count, 10]
    X = X.tolist()
    x_train = data.iloc[idx:idx + count, 0:8]
    prediction = model.predict(x_train)
    prediction = prediction.tolist()
    return jsonify({"Y": prediction,"X":X})

# @app.route('/api/predict2/', methods=['GET'])
# def predict2():
#     # return "count is " + count
#     # x = current_row
#     params = request.args.to_dict()
#     print(params)
#     type = params["type"]
#     from_year = params["fyear"]
#     from_month = params["fmonth"]
#     to_year = params["tyear"]
#     to_month = params["tmonth"]
#     st = 0
#     en = 0
#     for i in range(len(data)):
#         if data.iloc[i, 0] == from_year and data.iloc[i, 1] == from_month:
#             st = i
#             break
#     for i in range(len(data)):
#         if data.iloc[i, 0] == to_year and data.iloc[i, 1] == to_month:
#             en = i
#             break
#     idx = st
#     count = en - st
#     x_train = data.iloc[idx:idx + count, 0:8]
#     prediction = model.predict(x_train)
#     prediction = prediction.tolist()
#     # print(prediction.shape)
#     # output =prediction
#     # output = round(prediction[0], 2)
#     return jsonify({"Deposits ": prediction})




if __name__ == '__main__':
    app.run(debug=True)