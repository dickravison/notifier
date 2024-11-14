import json
import os
import requests

AWS_SESSION_TOKEN = os.environ.get('AWS_SESSION_TOKEN')
SSM_URL = 'http://localhost:2773/systemsmanager/parameters/get?withDecryption=true&name='
API_URL = 'https://api.pushover.net/1/messages.json'
USER_PARAM = '/notifier/user'
TOKEN_PARAM = '/notifier/token'

#Loop over each record in the event and push the message to Pushover
def notify(event, context):
    for e in event['Records']:
        headers = {'X-Aws-Parameters-Secrets-Token':AWS_SESSION_TOKEN}
        response = requests.get(SSM_URL + USER_PARAM, headers = headers)
        user = json.loads(response.text)
        response = requests.get(SSM_URL + TOKEN_PARAM, headers = headers)
        token = json.loads(response.text)

        message = e['Sns']['Message']
        subject = e['Sns']['Subject']
        payload = {"title": subject, "message": message, "user": user['Parameter']['Value'], "token": token['Parameter']['Value'] , "html": "1"}
        r = requests.post(API_URL, data=payload, headers={'User-Agent': 'Python'})
        print(r)