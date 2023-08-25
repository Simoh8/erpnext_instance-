# import requests
# import frappe 
# import erpnext

# import requests

# payout_url = "https://api.sandbox.pawapay.cloud/payouts"

# payload = {
#   "payoutId": "f4401be2-1568-4140-bf2d-eb77d2b2b639",
#   "amount": "1500.21",
#   "currency": "KES",
#   "country": "KEN",
#   "correspondent": "MPESA_KEN",
#   "recipient": {
#     "type": "MSISDN",
#     "address": {
#       "value": "254742582849"
#     }
#   },
#   "customerTimestamp": "2020-02-21T17:32:28Z",
#   "statementDescription": "Up to 22 chars note"
# }

# headers = {
#   "Content-Type": "application/json",
#   "Authorization": "Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJqdGkiOiI4ODZiZmIyNS1kNWRlLTQ3YjYtODBlMy1iN2JhNmRhYTk0ZjUiLCJzdWIiOiIxNTYiLCJpYXQiOjE2OTI2NDc2ODksImV4cCI6MjAwODI2Njg4OSwicG0iOiJEQUYsUEFGIiwidHQiOiJBQVQifQ.PC-Yp0rd8ZnZ75lKHPEkltS_iczls59yjyFSk4ur86w "
# }

# response = requests.post(payout_url, json=payload, headers=headers)

# data = response.json()
# print(data)



# import requests

# url = "https://api.sandbox.pawapay.cloud/deposits"

# payload = {
#   "depositId": "f4401bd2-1178-4140-bf2d-eb77d2b2b639",
#   "amount": "15.21",
#   "currency": "KES",
#   "country": "KEN",
#   "correspondent": "MPESA_KEN",
#   "payer": {
#     "type": "MSISDN",
#     "address": {
#       "value": "254742582849"
#     }
#   },
#   "customerTimestamp": "2020-02-21T17:32:28Z",
#   "statementDescription": "Up to 22 chars note",
#   # "preAuthorisationCode": "QJS3RSKZXY"
# }

# response = requests.post(url, json=payload, headers=headers)

# data = response.json()
# print(data)


# def process_payment(payment_data):
#     # Your logic to process payment data here
#     # Example: Save payment_data to the database
#     return {"status": "success", "message": "Payment processed successfully"}


# import http.client
# import json

# conn = http.client.HTTPSConnection("api.sandbox.pawapay.cloud")
# payload = json.dumps({
#   "payoutId": "f44051bd9-956-4140-bf2d-eb77d2b2b639",
#   "amount": "10",
#   "currency": "KES",
#   "country": "KEN",
#   "correspondent": "MPESA_KEN",
#   "recipient": {
#     "type": "MSISDN",
#     "address": {
#       "value": "254742582849"
#     }
#   },
#   "customerTimestamp": "2023-02-21T17:32:28Z",
#   "statementDescription": "Up to 22 chars note"
# })
# headers = {
#   'Authorization': 'Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJqdGkiOiI4ODZiZmIyNS1kNWRlLTQ3YjYtODBlMy1iN2JhNmRhYTk0ZjUiLCJzdWIiOiIxNTYiLCJpYXQiOjE2OTI2NDc2ODksImV4cCI6MjAwODI2Njg4OSwicG0iOiJEQUYsUEFGIiwidHQiOiJBQVQifQ.PC-Yp0rd8ZnZ75lKHPEkltS_iczls59yjyFSk4ur86w',
#   'Content-Type': 'application/json'
# }
# conn.request("POST", "/payouts", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))


# from erpnext import erpnext.accounts.doctype.payment_entry

import frappe
from .api_data_endpoint import api_data_endpoint

@frappe.whitelist(allow_guest=True)
def api_data_endpoint(data):
    try:
        # Process the received data here
        # Example: Save the data to your custom app's database
        response_data = {"status": "success", "message": "Data received successfully"}
        return response_data
    except Exception as e:
        return {"status": "error", "message": str(e)}

