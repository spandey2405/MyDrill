import requests
import json
r = requests.get("https://graph.facebook.com/v2.4/275476105939521/feed?format=json&access_token=717690628267029|Ms4V8xoBgdW1RT7mFhMzc8QgoUA&limit=25&until=1441464431&__paging_token=enc_AdBcVahdTTjLrA9tDOZC52qZBcjM5qo6Dm3LTB5fUQJc9V28yaBfzP6c4PwOCsBLlHXiaFGLZBWbVfYv4tqu1ZBCWskyknCyuYZCfnAoekZAfZB20gFCgZDZD")

data = r.json()

for post in data["data"]:
 print 