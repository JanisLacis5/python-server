import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .ibkr_file.ibkr_file import read_ibkr_file
from .tradingview_file.trw_file import read_trw_file

ibkr_file_path = r'C:\Users\lacis\Documents\EASYTRADING\pythonserver\pyserver\pyserver\ibkr_file\file.csv'
trw_file_path = r'C:\Users\lacis\Documents\EASYTRADING\pythonserver\pyserver\pyserver\tradingview_file\trw.csv'


@csrf_exempt
def send_ibkr_file_data(req):
    req_data = json.loads(req.body)
    req_data = req_data['file']
    with open('./temp.csv', 'w') as f:
        f.write(req_data)

    with open('./temp.csv') as file:
        stripped = [f'{line.strip().replace(',', '')},' for line in file if line.strip() != '']
        with open(ibkr_file_path, 'w') as f:
            for line in stripped:
                f.write(line)

    res = read_ibkr_file()
    return HttpResponse(json.dumps({'data': res}))


@csrf_exempt
def send_trw_file_data(req):
    req_data = json.loads(req.body)
    req_data = req_data['file']
    with open(trw_file_path, 'w') as file:
        file.write(req_data)

    res = read_trw_file()
    return HttpResponse(json.dumps({'data': res}))
