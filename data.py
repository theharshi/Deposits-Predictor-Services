import pandas as pd
from pandas.io.parsers import read_csv


def create_data():
    data = pd.read_csv('./assets/complete_dataset_1.csv')
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
    data['date'] = DATE
    del data['Date']
    return data