from datetime import datetime
import pandas as pd


def read_ibkr_file():
    csv_path = r'C:\Users\lacis\Documents\EASYTRADING\pythonserver\pyserver\pyserver\ibkr_file\file.csv'
    file = pd.read_csv(csv_path)
    file_content = file.columns[3:-1]
    print(file_content)

    ret_list = []

    for i, line in enumerate(file_content):
        line = line.split('|')
        if len(line) > 1:
            ticker = line[2]
            action = 'long' if line[5][:3] == 'BUY' else 'short'
            date = datetime.strptime(line[7], "%Y%m%d").strftime("%d-%m-%Y")
            time = line[8][:5]
            price = round(float(line[12]) * int(line[10][:-3]), 2)
            ret_list.append([date, time, ticker, price, action])

    calc_list = []

    while len(ret_list) > 1:
        trade = ret_list[0]
        first_opposite_action = None
        first_opposite_action_index = None

        for i, row in enumerate(ret_list):
            if row[-1] != trade[-1] and row[2] == trade[2]:
                first_opposite_action = row
                first_opposite_action_index = i
                break

        date = first_opposite_action[0]
        time = first_opposite_action[1]
        symbol = trade[2]
        action = trade[-1]
        pl = round(first_opposite_action[3] + trade[3], 2)
        pl = pl * -1 if first_opposite_action[3] < trade[3] and action == 'long' else pl * 1
        pl = pl * -1 if first_opposite_action[3] > trade[3] and action == 'short' else pl * 1

        ret_list.pop(0)
        ret_list.pop(first_opposite_action_index - 1)

        calc_list.append({'date': date, 'time': time, 'symbol': symbol, 'pl': pl, 'action': action})

    return calc_list
