# Request module must be installed.
# Run pip install requests if necessary.
import requests

subscription_key = '9fcaa2e999634c389f2588d46ead7ecf'


def get_token(subscription_key):
    fetch_token_url = 'https://uksouth.api.cognitive.microsoft.com/sts/v1.0/issueToken'
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'X-Microsoft-OutputFormat': 'audio-16khz-128kbitrate-mono-mp3',
        'User-Agent':'curl'
    }
    data = {
        '<speak version': '\\1.0\'''',
        'lang':"en-US",
        'name': 'en-US-AriaRUS',
        'voice':'For the Tytanyum glory'
    }
    response = requests.post(fetch_token_url, headers=headers, data=data)
    access_token = str(response.text)
    print(response)

