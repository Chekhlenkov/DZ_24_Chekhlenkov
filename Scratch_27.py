import requests
url = "http://127.0.0.1:5000/perform_query"
payload = {
    'file_name': 'apache_logs.txt',
    'queries':[
        {
            'cmd': 'regex',
            'value': 'images/\\w+\\.png'
        }
    ],
}
response = requests.request("POST", url, json=payload)
print(response.text)