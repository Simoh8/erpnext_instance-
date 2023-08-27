import frappe
import requests
@frappe.whitelist(allow_guest=True)
def api_data_endpoint(data):
    try:
        print(data)
        print(data[1])
        response_data = {"status": "success", "meapi_data_endpointssage": "Data received successfully"}
        return response_data
    except Exception as e:
        return {"status": "error", "message": str(e)}


payload = {
  "payoutId": "f4401bd2-1568-4140-bf2d-eb77d2b2b639",
  "amount": "15.21",
  "currency": "ZMW",
  "country": "ZMB",
  "correspondent": "MTN_MOMO_ZMB",
  "recipient": {
    "type": "MSISDN",
    "address": {
      "value": "256780334452"
    }
  },
  "customerTimestamp": "2020-02-21T17:32:28Z",
  "statementDescription": "Up to 22 chars note"
}

url = "https://api.sandbox.pawapay.cloud/payouts"
headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJqdGkiOiI4ODZiZmIyNS1kNWRlLTQ3YjYtODBlMy1iN2JhNmRhYTk0ZjUiLCJzdWIiOiIxNTYiLCJpYXQiOjE2OTI2NDc2ODksImV4cCI6MjAwODI2Njg4OSwicG0iOiJEQUYsUEFGIiwidHQiOiJBQVQifQ.PC-Yp0rd8ZnZ75lKHPEkltS_iczls59yjyFSk4ur86w"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
status=data["status"]

amount = payload["amount"]
recipient_value = payload["recipient"]["address"]["value"]

# Create a transaction dictionary
transaction = {
    "amount": amount,
    "recipient_value": recipient_value
}

if status == "ACCEPTED":
    print(f"The transaction of {amount} on phone number {recipient_value} is successful".lower())
else:
    print(f"The transaction of {amount} on phone number {recipient_value} has been {status} please try again later".lower())
