### 3.1 Setting Up the Environment

import requests
import json
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from urllib.parse import urljoin

edgerc = EdgeRc('.edgerc')
section = 'idm'
baseurl = 'https://{}'.format(edgerc.get(section, 'host') )

session = requests.Session()
session.auth = EdgeGridAuth.from_edgerc(edgerc, section)

# print(baseurl)

client_id='e4zlatds7ky33his'



### 3.2 Getting Credential ID

path='/identity-management/v1/open-identities/{}/credentials'.format(client_id)
# print(path)

url=urljoin(baseurl, path)
# print(url)

ret = session.get( url )
ret_json = json.dumps( ret.json(), indent=2 )
print( ret_json )




### 3.3 Updating Expiry Date

body=json.loads('''
  {
    "credentialId": 914339,
    "clientToken": "akab-hdmugzwjqnbw62dw-ixiz5fmwq2edfj6g",
    "status": "ACTIVE",
    "createdOn": "2020-09-03T01:36:23.000Z",
    "description": "",
    "expiresOn": "2023-01-01T00:00:00.000Z"
  }
''')

cred_id = 914339
path='/identity-management/v1/open-identities/{}/credentials/{}'.format(client_id, cred_id)
url = urljoin(baseurl, path)
# print(url)

ret = session.put(url, json=body)
print( ret.status_code )





