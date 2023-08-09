import os
import json
import requests
url = input("Enter  URL:")
link=input("Enter Mask URL:")
res=json.loads(requests.get("https://is.gd/create.php?format=json&url="+url).content.decode("utf-8"))
shorturl=res["shorturl"]
print(shorturl)
mask=shorturl[8:]
print(link+"@"+mask)
