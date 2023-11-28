import pandas as pd

full_file_path = r'C:\users\lacis\Documents\EASYTRADING\pythonserver\pyserver\pyserver\tradingview_file\trw.csv'


def read_trw_file():
    file = pd.read_csv(full_file_path)
    ret_list = []
    for i, line in file.iterrows():
        date, time = line['Time'].split(' ')
        action = line['Action'].split(' ')[1]
        symbol = line['Action'].split(' ')[5].split(':')[1]
        pl = float(line['P&L'])
        ret_list.append({'date': date, 'time': time[:5], 'symbol': symbol, 'pl': pl, 'action': action})
    return ret_list
