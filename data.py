import datetime

import pandas as pd
from pandas.io.parsers import read_csv
# {
#     "frequency": 0,
#     "count": 3,
#     "type": 2,
#     "columns": [
#          "Interest Inflation Gap",
#         "Average Pay",
#         "Employment Rate"
#     ],
#     "features": [
#         [
#             100,
#             -0.5,
#             90
#         ],
#         [
#             120,
#             -0.55,
#             89
#         ],
#         [
#             110,
#             -0.45,
#             88
#         ]
#     ]
# }
def create_data(params):
    count = params["count"]
    freq = params["frequency"]
    type = params["type"]
    dict = {}
    dict[0] = 7
    dict[1] = 30
    dict[2] = 365
    gap = []
    pay = []
    employment = []
    for i in range(count):
        for j in range(dict[freq]):
            gap.append(params["features"][0][i])
    for i in range(3):
        for j in range(dict[freq]):
            pay.append(params["features"][1][i])
    for i in range(3):
        for j in range(dict[freq]):
            employment.append(params["features"][2][i])

    data = {
        params["columns"][0]: gap,
        params["columns"][1]: pay,
        params["columns"][2]: employment,
    }
    base = datetime.date.today()
    df = pd.DataFrame(data)
    # print(startDate)
    dates = []
    for i in range(count * dict[freq]):
        next_date = base + datetime.timedelta(i)
        dates.append(next_date.strftime('%d-%m-%Y'))

    df = pd.DataFrame(data)
    day = pd.to_datetime(dates, format="%d-%m-%Y").day
    month = pd.to_datetime(dates, format="%d-%m-%Y").month
    year = pd.to_datetime(dates, format="%d-%m-%Y").year
    df.insert(0, 'Day', day)
    df.insert(0, 'Year', year)
    df.insert(0, 'Month', month)
    print(df)
    # del df['Year']
    return df,dates
