from urllib.parse import urlparse, urljoin
import sys
import json

with open("LinearEquationSolverIntegrationRequireAPIKey.postman_collection_template.json") as file:
    collection = json.load(file)

request = collection["item"][0]["request"]
url = request["url"]

api = sys.argv[1]
stage = sys.argv[2]

api_key = sys.argv[3]
request["auth"]["apikey"][0]["value"] = api_key

parts = urlparse(api)

print(parts)

path = parts.path.strip("/")

if len(path) > 0:
    url["raw"] = api
    url["path"][0] = path
    
    if not stage in path:
        print("The given API Gateway stage name is different from the alias of the associated Lambda function.")
else:
    url["raw"] = urljoin(api, stage)
    url["path"][0] = stage

    print("The stage name was not part of the API Gateway url, so we assume it is the same as the associated Lambda function alias")

url["protocol"] = parts.scheme
url["host"] = parts.hostname.split(".")

with open("LinearEquationSolverIntegrationRequireAPIKey.postman_collection.json", "w") as file:
    json.dump(collection, file)


