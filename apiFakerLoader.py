import json
import requests
import sys

baseurl = "http://localhost:3000"
url = baseurl + "/hello"
testpush = baseurl + "/testendpoint"

try:
    response = requests.get(url)
except ConnectionRefusedError:
    print("Connection to API Faker refused, is it running at all?")
    sys.exit()
except Exception:
    print("Something blew up!!")
    sys.exit()

if response.status_code != 200:
    print("API Faker not online, check that it is running")
    sys.exit()
else:
    print("API Faker online, now can begin to load up with fake endpoints")

pushdata = {
    "name" : "Jamie",
    "DOB" : "7 Oct 1976"
}

header = {
    "Content-Type" : "application/json"
}

print("Attempting to send " + json.dumps(pushdata))
pushresponse = requests.put(url=testpush, json=pushdata, headers=header)
if pushresponse.status_code == 200:
    print("Push was successful, here's the body in the return")
    print(pushresponse.content)