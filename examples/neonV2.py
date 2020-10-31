############## ATXHS NeonCRM API Integrations ###############
# Neon API v2 docs - https://developer.neoncrm.com/api-v2/ #
###########################################################

import requests
import json
from pprint import pprint
import hashlib
import base64
import time
import hmac


## Helper function for API calls
def apiCall(httpVerb, url, data, headers):
    # Make request
    if httpVerb == 'GET':
        response = requests.get(url, data=data, headers=headers)
    elif httpVerb == 'POST':
        response = requests.post(url, data=data, headers=headers)
    elif httpVerb == 'PUT':
        response = requests.put(url, data=data, headers=headers)
    elif httpVerb == 'PATCH':
        response = requests.patch(url, data=data, headers=headers)
    elif httpVerb == 'DELETE':
        response = requests.delete(url, data=data, headers=headers)
    else:
        print(f"HTTP verb {httpVerb} not recognized")

    response = response.json()
    print(response)

    return response


# Neon API v2.1 - Request Info
neonApiKey = ''
orgid = 'atxhs'
auth = f'{orgid}:{neonApiKey}'
baseURL = 'https://api.neoncrm.com/v2'
signature = base64.b64encode(bytearray(auth.encode())).decode()
headers = {'Content-Type':'application/json','Authorization': f'Basic {signature}', 'NEON-API-VERSION': '2.1'}


# Get list of custom fields
httpVerb = 'GET'
resourcePath = '/customFields'
queryParams = '?category=Account'
data = ''
url = baseURL + resourcePath + queryParams

response = apiCall(httpVerb, url, data, headers)