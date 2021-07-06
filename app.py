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

# data = create_data()
@app.route('/')
def home():
    return 'Hello World'
# @app.route('/api/predict/<int:type>/<int:count>',methods = ['GET'])
# def predict(count):
#     x_train = data.iloc[0:count,0:8]
#     model = pickle.load(open(Models[type], 'rb'))
#     prediction = model.predict(x_train)
#     prediction = prediction.tolist()
#     return jsonify({" predictions " : prediction })
#
#
# @app.route('/api/predict_date/<int:type>/<fromDate>/<toDate>', methods=['GET'])
# def predict_date(type,fromDate,toDate):
#     idx = 0
#     st = 0
#     en = 0
#     for i in range(len(data)):
#         if data.iloc[i, 10] == fromDate :
#             st = i
#             break
#     for i in range(len(data)):
#         if data.iloc[i, 10] == toDate :
#             en = i
#             break
#     count = en - st
#     idx = st
#     model = pickle.load(open(Models[type], 'rb'))
#     print("count ",count)
#     print("st en ",st, " ",en)
#     X = data.iloc[idx:idx + count, 10]
#     X = X.tolist()
#     x_train = data.iloc[idx:idx + count, 0:8]
#     prediction = model.predict(x_train)
#     prediction = prediction.tolist()
#     return jsonify({"Y": prediction,"X":X})

@app.route('/api/predict2/', methods=['GET','POST'])
def predict2():
    params = request.get_json(force=True)
    x_test,dates = create_data(params=params)
    type = params["type"]
    model = pickle.load(open(Models[type], 'rb'))
    y_pred = model.predict(x_test)
    y_pred = y_pred.tolist()
    print(y_pred)
    return jsonify({"Y": y_pred,"X":dates})





if __name__ == '__main__':
    app.run(debug=True)