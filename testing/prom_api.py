import json
import requests

data = requests.get('http://g.cmaker.studio:9090/api/v1/alerts')
json_data = json.loads(data.content)
print(json_data)