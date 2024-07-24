import requests
import json

"""
Build the Docker image: docker build --platform linux/amd64 -t docker-image . --target production
Run image locally: docker run --platform linux/amd64 -p 9000:8080 docker-image 

Test: run this script to test the running image
"""

payload = {"eqn": "x^3 - 1=0"}

# The equation is in the body
r = requests.get("http://localhost:9000/2015-03-31/functions/function/invocations", json=payload)

print(r.json())
print(r.request.headers)

print("\n\n\n")

# The equation is the query string: This does not work
headers = {"Content-Type": "application/json"}
#headers = {"Content-Type": "text/html"}
r0 = requests.get("http://localhost:9000/2015-03-31/functions/function/invocations", params=payload, headers=headers)

print(r0.url)
print(r0.json())
print(r0.request.headers)