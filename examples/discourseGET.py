import requests
import json

# Account Info
APIkey =''
APIuser =''
baseURL = 'yo.atxhs.org'

# Request Info
httpVerb ='GET'
resourcePath = '/admin/users/list/active.json'
data = ''

# Construct URL 
url = f'https://{baseURL}{resourcePath}'

# Construct headers
# POST headers
# headers = {'Content-Type':'multipart/form-data;','Api-Key':APIkey,'Api-Username':APIuser}
# GET headers
headers = {'Api-Key':APIkey,'Api-Username':APIuser}

# Make request
response = requests.get(url, data=data, headers=headers)
response = response.json()

# (Optional) Print to file
with open('../private/users.json', 'w') as outfile:
    json.dump(response, outfile, indent=4)