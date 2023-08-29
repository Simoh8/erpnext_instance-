# import uuid
# import frappe
# from frappe.utils.data import now
# import requests
# from frappe.model.mapper import get_mapped_doc


# @frappe.whitelist(allow_guest=True)
# def api_data_endpoint(data):
#     try:
#         print(data)
#         payload_id = str(uuid.uuid4())
#         payload = {
#             "payoutId": payload_id,
#             "amount": "15.21",
#             "currency": "KES",
#             "country": "KEN",
#             "correspondent": "MPESA_KEN",
#             "recipient": {
#                 "type": "MSISDN",
#                 "address": {
#                     "value": "254742582849"
#                 }
#             },
#             "customerTimestamp": "2023-02-21T17:32:28Z",
#             "statementDescription": "Up to 22 chars note"

#         }
        
#         url = "https://api.sandbox.pawapay.cloud/payouts"
#         headers = {
#             "Content-Type": "application/json",
#             "Authorization": ""
#         }
        
#         response = requests.post(url, json=payload, headers=headers)
#         response_data = response.json()
#         status = response_data["status"]
#         amount = payload["amount"]
#         recipient_value = payload["recipient"]["address"]["value"]
        
#         if status == "ACCEPTED":

#             payment_entry_data = {
#                 "doctype": "Payment Entry",
#                 "paid_amount": amount,
#                 "party_type": "Student",  
#                 "party": "EDU-STU-2023-00001",  
#                 "payment_type": "Receive",
#                 "received_amount": 200,
#                 "target_exchange_rate": 50.60,
#                 "posting_date": now(),
#                 "paid_to": "simon",  
#                 "paid_to_account_currency": "ZMW"
#             }

#             print(payment_entry_data)

#             # Create Payment Entry in ERPNext using API
#             erp_url = "http://192.168.100.143:8000/api/resource/Payment%20Entry"
#             erp_headers = {
#                 "Content-Type": "application/json",
#                 "Authorization": "Token 03ed72a3f5eb4b4:b1e65c13cb80575"
#             }

#             erp_response = requests.post(erp_url, json=payment_entry_data, headers=erp_headers)
#             erp_data = erp_response.json()

#             if erp_response.status_code == 200:
#                 print("Payment Entry created in ERPNext:", erp_data)

#                 # Call the make_payment_order function
#                 make_payment_order(erp_data.get("data").get("name"))

#             else:
#                 print("Error creating Payment Entry in ERPNext:", erp_data)
            
#             print(f"The transaction of {amount} on phone number {recipient_value} is successful".lower())
            
#         else:
#             print(f"The transaction of {amount} on phone number {recipient_value} has been {status}. Please try again later".lower())
        
#         response_data = {"status": "success", "message": "Data received successfully"}
#         return response_data
        
#     except Exception as e:
#         return {"status": "error", "message": str(e)}

# @frappe.whitelist()
# def make_payment_order(source_name, target_doc=None):
#     def set_missing_values(source, target):
#         target.payment_order_type = "Payment Entry"
#         target.append(
#             "references",
#             dict(
#                 reference_doctype="Payment Entry",
#                 reference_name=source.name,
#                 bank_account=source.party_bank_account,
#                 amount=source.paid_amount,
#                 account=source.paid_to,
#                 supplier=source.party,
#                 mode_of_payment=source.mode_of_payment,
#             ),
#         )

#     doclist = get_mapped_doc(
#         "Payment Entry",
#         source_name,
#         {
#             "Payment Entry": {
#                 "doctype": "Payment Order",
#                 "validation": {"docstatus": ["=", 1]},
#             }
#         },
#         target_doc,
#         set_missing_values,
#     )

# # Call the API data processing function
# # api_data_endpoint("Sample Data")



import frappe
import uuid
from frappe.utils.data import now
import requests
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist(allow_guest=True)
def api_data_endpoint(data):
    try:
        print(data)
        # Generate UUIDv4 for payloadId
        payload_id = str(uuid.uuid4())
        amount = data["amount"]
        
        payload = {
            "payoutId": payload_id,
            "amount": amount,
            "currency": "KES",
            "country": "KEN",
            "correspondent": "MPESA_KEN",
            "recipient": {
                "type": "MSISDN",
                "address": {
                    "value": "254742582849"
                }
            },
            "customerTimestamp": "2023-02-21T17:32:28Z",
            "statementDescription": "Up to 22 chars note"

        }
        
        url = "https://api.sandbox.pawapay.cloud/payouts"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJqdGkiOiI4ODZiZmIyNS1kNWRlLTQ3YjYtODBlMy1iN2JhNmRhYTk0ZjUiLCJzdWIiOiIxNTYiLCJpYXQiOjE2OTI2NDc2ODksImV4cCI6MjAwODI2Njg4OSwicG0iOiJEQUYsUEFGIiwidHQiOiJBQVQifQ.PC-Yp0rd8ZnZ75lKHPEkltS_iczls59yjyFSk4ur86w"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        status = response_data["status"]
        
        recipient_value = payload["recipient"]["address"]["value"]
        
        if status == "ACCEPTED":
            print(f"The transaction of {amount} on phone number {recipient_value} is successful".lower())
            
            # Create Payment Entry in ERPNext
            create_payment_entry(amount, recipient_value)
            
        else:
            print(f"The transaction of {amount} on phone number {recipient_value} has been {status}. Please try again later".lower())
        
        response_data = {"status": "success", "message": "Data received successfully"}
        return response_data
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

def create_payment_entry(amount, recipient_value):
    # payment_entry_data dictionary
    payment_entry_data = {
        "doctype": "Payment Entry",
        "paid_amount": amount,
        "party_type": "Student",  
        "party": "EDU-STU-2023-00001",  
        "payment_type": "Receive",
        "received_amount": 200,
        "target_exchange_rate": 50.60,
        "posting_date": now(),
        "paid_to": "simon",  
        "paid_to_account_currency": "ZMW"
    }

    # Payment Entry in ERPNext using API
    erp_url = "http://192.168.100.16:8000/app/payment-entry"
    erp_headers = {
        "Content-Type": "application/json",
        "Authorization": "Token 75f56297:a476137883a465c"
    }
    erp_response = requests.post(erp_url, json=payment_entry_data, headers=erp_headers)
    erp_data = erp_response.json()

    if erp_response.status_code == 200:
        print("Payment Entry created in ERPNext:", erp_data)
    else:
        print("Error creating Payment Entry in ERPNext:", erp_data)
