import json
import os
import requests

AWS_SESSION_TOKEN = os.environ.get('AWS_SESSION_TOKEN')
NOTIFICATIONS_ENABLED = os.environ.get('NOTIFICATIONS_ENABLED')
SSM_URL = 'http://localhost:2773/systemsmanager/parameters/get?withDecryption=true&name='
API_URL = 'https://api.pushover.net/1/messages.json'
HEADERS = {
    "User-Agent": "Python"
}
USER_PARAM = '/notifier/user'
TOKEN_PARAM = '/notifier/token'

def notify(event, context):
    #Retrieve the API credentials from AWS Parameter Store
    headers = {'X-Aws-Parameters-Secrets-Token':AWS_SESSION_TOKEN}
    response = requests.get(SSM_URL + USER_PARAM, headers = headers)
    user = json.loads(response.text)
    response = requests.get(SSM_URL + TOKEN_PARAM, headers = headers)
    token = json.loads(response.text)
    #Loop over each event and publish a new message to the SNS topic
    for e in event['Records']:
        message = e['Sns']['Message']
        subject = e['Sns']['Subject']
        payload = {"title": subject, "message": message, "user": user['Parameter']['Value'], "token": token['Parameter']['Value'] , "html": "1"}
        r = requests.post(API_URL, data=payload, headers=HEADERS)
        print(r)
