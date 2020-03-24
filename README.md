# python_twitcasting_apiv2
Reference: https://apiv2-doc.twitcasting.tv/

Example:
```python
import tc.apis
import tc.auth
from http.client import HTTPSConnection

auth = tc.auth.TCAppAuth(ClientID, ClientSecret)
conn = HTTPSConnection('apiv2.twitcasting.tv')
req  = tc.apis.get_user_info(auth, 'some_user')
conn.request(req.method, req.url, req.body, req.headers)
resp = conn.getresponse()
data = resp.read()
conn.close()

print(data)
```
