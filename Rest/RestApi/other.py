import requests
import json
BASE_URL="http://127.0.0.1:8000/empapi/"
HEADERS={'content-type':'application/json'}

def get_data(id=None):
    json_data={}
    if id:
        json_data={'id':id}
    url=f'{BASE_URL}'
    response=requests.get(url=url,headers=HEADERS,data=json.dumps(json_data))
    new_data=response.json()
    print(new_data)
get_data()
def post_data():
    url=f'{BASE_URL}'
    data={
        'name':'piyush raj',
        'mobile':8073399259,
        'city':'Bangalore'
    }
    json_data = json.dumps(data)
    response = requests.post(url=url,headers=HEADERS, data=json_data)
    print(response)
    res = response.json()
    print(f'result is {res}')
#post_data()
