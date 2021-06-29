import requests
import json
BASE_URL="http://127.0.0.1:8000/signupapi"
HEADERS={'content-type':'application/json'}

def post_data():
    url=f'{BASE_URL}'
    data={
        'USERNAME':'piyushraj',
        'FIRST NAME':'Sid',
        'LAST NAME':'pati',
        'EMAIL ADDRESS':'gourav@gmail.com',
        'Pasword':123

    }
    json_data = json.dumps(data)
    response = requests.post(url=url,headers=HEADERS, data=json_data)
    print(response)
    res = response.json()
    print(f'result is {res}')
post_data()