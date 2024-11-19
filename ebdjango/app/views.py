from django.shortcuts import render
import json
import requests

def home(request):
    if request.method == 'POST':
        senddata = request.POST.get('data')
        data = json.loads(senddata)

        res = requests.post('https://aigy7q90l6.execute-api.us-east-2.amazonaws.com/PREDICT/predict', json=senddata)

        if res.status_code == 200:
            return render(request, 'cc.html', {'data':data, 'response':int(res.json())})
        else:
            return render(request, 'cc.html', {'error':res.json()})
    return render(request, 'cc.html', {'respone': False})
