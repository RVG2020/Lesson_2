
import flask
import requests
import jsons
'''"GBP": {
            "ID": "R01035",
            "NumCode": "826",
            "CharCode": "GBP",
            "Nominal": 1,
            "Name": "Фунт стерлингов Соединенного королевства",
            "Value": 82.9866,
            "Previous": 82.2263'''


url='https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = jsons.loads(response.text)
print ('готово')