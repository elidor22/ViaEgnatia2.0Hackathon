import requests, uuid, json
from AzureCognitive import toTranslate
# Class is redundant

# Add your subscription key and endpoint
subscription_key = "f4ffcd5b08554f6da675438c0e1937f9"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "westeurope"

path = '/translate'
constructed_url = endpoint + path
text = 'The ancient city of Apollonia is situated in southwestern Albania, about 13 miles from the city of Fier. The fascinating landscape of the archeological park, which has been preserved in an exceptionally intact condition, comprises a successful combination between the beauty of monuments and nature, attractive through its long history, in an atmosphere of relaxation and meditation. Its foundation took place immediately after the foundation of Epidamnus – Dyrrachium and quickly became one of the most eminent cities of the Adriatic basin, which was mentioned more frequently from the other 30 (thirty) cities bearing the same name during Antiquity. The city lay in the territory of the political communion of the Taulantii and was broadly known as Apollonia of Illyria. According to the tradition it was founded during the first half of the 6th century BC by Greek colonist from Corfu and Corinth, led by Gylax, which named the city after his name (Gylakeia). After its quick establishment the city changed its name to Apollonia, according to the powerful divinity Apollo. It stands on a hilly plateau from where expands the fertile plain of Musacchia with the Adriatic Sea and the hills of Mallakastra. The ruins of Apollonia are discovered in the beginning of the 19th century.'
params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['fr','de','jp']
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': text
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

# Trying to get e single value from the response
tst = response[0]
