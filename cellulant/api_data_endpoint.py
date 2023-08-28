# # import frappe
# # import requests

# # @frappe.whitelist(allow_guest=True)
# # def api_data_endpoint(data):
# #     try:
# #         print(data)
# #         response_data = {"status": "success", "message": "Data received successfully"}
# #         return response_data
# #     except Exception as e:
# #         return {"status": "error", "message": str(e)}

# # payload = {
# #   "payoutId": "f4401bd2-1568-4140-bf2d-eb77d2b2b639",
# #   "amount": "15.21",
# #   "currency": "ZMW",
# #   "country": "ZMB",
# #   "correspondent": "MTN_MOMO_ZMB",
# #   "recipient": {
# #     "type": "MSISDN",
# #     "address": {
# #       "value": "256780334452"
# #     }
# #   },
# #   "customerTimestamp": "2020-02-21T17:32:28Z",
# #   "statementDescription": "Up to 22 chars note"
# # }

# # url = "https://api.sandbox.pawapay.cloud/payouts"
# # headers = {
# #   "Content-Type": "application/json",
# #   "Authorization": "Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJqdGkiOiI4ODZiZmIyNS1kNWRlLTQ3YjYtODBlMy1iN2JhNmRhYTk0ZjUiLCJzdWIiOiIxNTYiLCJpYXQiOjE2OTI2NDc2ODksImV4cCI6MjAwODI2Njg4OSwicG0iOiJEQUYsUEFGIiwidHQiOiJBQVQifQ.PC-Yp0rd8ZnZ75lKHPEkltS_iczls59yjyFSk4ur86w"
# # }

# # response = requests.post(url, json=payload, headers=headers)
# # data = response.json()
# # status = data["status"]

# # amount = payload["amount"]
# # recipient_value = payload["recipient"]["address"]["value"]

# # # Create a transaction dictionary
# # transaction = {
# #     "amount": amount,
# #     "recipient_value": recipient_value,
# #     "party":"student",
# #     "payment_type":"Receive",
# #     # "party_name":data["Student_id"]
# # }

# # # Now, you can use the 'transaction' dictionary for further processing or logging
# # print("Initialized transaction:", transaction)
# # if status == "ACCEPTED":
# #     print(f"The transaction of {amount} on phone number {recipient_value} is successful".lower())
# # else:
# #     print(f"The transaction of {amount} on phone number {recipient_value} has been {status} please try again later".lower())
# import frappe
# import requests
# from frappe.model.mapper import get_mapped_doc

# @frappe.whitelist(allow_guest=True)
# def api_data_endpoint(data):
#     try:
#         print(data)
        
#         payload = {
#             "payoutId": "f4401bd2-1568-4140-bf2d-eb77d2b2b639",
#             "amount": "15.21",
#             "currency": "ZMW",
#             "country": "ZMB",
#             "correspondent": "MTN_MOMO_ZMB",
#             "recipient": {
#                 "type": "MSISDN",
#                 "address": {
#                     "value": "256780334452"
#                 }
#             },
#             "customerTimestamp": "2020-02-21T17:32:28Z",
#             "statementDescription": "Up to 22 chars note"
#         }
        
#         url = "https://api.sandbox.pawapay.cloud/payouts"
#         headers = {
#             "Content-Type": "application/json",
#             "Authorization": "Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJqdGkiOiI4ODZiZmIyNS1kNWRlLTQ3YjYtODBlMy1iN2JhNmRhYTk0ZjUiLCJzdWIiOiIxNTYiLCJpYXQiOjE2OTI2NDc2ODksImV4cCI6MjAwODI2Njg4OSwicG0iOiJEQUYsUEFGIiwidHQiOiJBQVQifQ.PC-Yp0rd8ZnZ75lKHPEkltS_iczls59yjyFSk4ur86w"
#         }
        
#         response = requests.post(url, json=payload, headers=headers)
#         data = response.json()
#         status = data["status"]
        
#         amount = payload["amount"]
#         recipient_value = payload["recipient"]["address"]["value"]
        
#         # Create a transaction dictionary
#         transaction = {
#             "amount": amount,
#             "recipient_value": recipient_value,
#             "party": "student",
#             "payment_type": "Receive",
#             # "party_name": data["Student_id"]
#         }
        
#         # Assuming you have received the necessary data for payment entry
#         payment_entry_data = {
#             "doctype": "Payment Entry",
#             "amount": amount,
#             "party_type": "Student",  # Adjust based on your ERP setup
#             # "party": "Student ID Here",  # Replace with actual student ID
#             "payment_type": "Receive",
#             # Add other necessary fields
#         }
        
#         # Create Payment Entry in ERPNext using API
#         erp_url = "http://192.168.100.143:8000/api/resource/Payment%20Entry"
#         erp_headers = {
#             "Content-Type": "application/json",
#             "Authorization": "Bearer 75f5ce19bc86297"
#         }
        
#         erp_response = requests.post(erp_url, json=payment_entry_data, headers=erp_headers)
#         erp_data = erp_response.json()
        
#         if erp_response.status_code == 200:
#             print("Payment Entry created in ERPNext:", erp_data)
            
#             # Call the make_payment_order function
#             make_payment_order(erp_data.get("data").get("name"))
        
#         else:
#             print("Error creating Payment Entry in ERPNext:", erp_data)
        
#         if status == "ACCEPTED":
#            @frappe.whitelist()
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
# api_data_endpoint("Simon Muturi")








#             print(f"The transaction of {amount} on phone number {recipient_value} is successful".lower())
#         else:
#             print(f"The transaction of {amount} on phone number {recipient_value} has been {status} please try again later".lower())
        
#         response_data = {"status": "success", "message": "Data received successfully"}
#         return response_data
        
#     except Exception as e:
#         return {"status": "error", "message": str(e)}

import frappe
import requests
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist(allow_guest=True)
def api_data_endpoint(data):
    try:
        print(data)
        
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
        response_data = response.json()
        status = response_data["status"]
        
        amount = payload["amount"]
        recipient_value = payload["recipient"]["address"]["value"]
        
        # Create a transaction dictionary
        transaction = {
            "amount": amount,
            "recipient_value": recipient_value,
            "party": "Student",
            "payment_type": "Receive",
            # "party_name": data["Student_id"]
        }
        
        # Assuming you have received the necessary data for payment entry
        payment_entry_data = {
            "doctype": "Payment Entry",
            "amount": amount,
            "party_type": "Student",  # Adjust based on your ERP setup
            "party": "EDU-STU-2023-00001",  # Replace with actual student ID
            "payment_type": "Receive",
            # Add other necessary fields
        }
        
        # Create Payment Entry in ERPNext using API
        erp_url = "http://192.168.100.143:8000/api/resource/Payment%20Entry"
        erp_headers = {
            "Content-Type": "application/json",
            "Authorization": "Token 75f5ce19bc86297:a476137883a465c"
        }
        
        erp_response = requests.post(erp_url, json=payment_entry_data, headers=erp_headers)
        erp_data = erp_response.json()
        
        if erp_response.status_code == 200:
            print("Payment Entry created in ERPNext:", erp_data)
            
            # Call the make_payment_order function
            make_payment_order(erp_data.get("data").get("name"))
        
        else:
            print("Error creating Payment Entry in ERPNext:", erp_data)
        
        if status == "ACCEPTED":
            print(f"The transaction of {amount} on phone number {recipient_value} is successful".lower())
        else:
            print(f"The transaction of {amount} on phone number {recipient_value} has been {status}. Please try again later".lower())
        
        response_data = {"status": "success", "message": "Data received successfully"}
        return response_data
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

@frappe.whitelist()
def make_payment_order(source_name, target_doc=None):
    def set_missing_values(source, target):
        target.payment_order_type = "Payment Entry"
        target.append(
            "references",
            dict(
                reference_doctype="Payment Entry",
                reference_name=source.name,
                bank_account=source.party_bank_account,
                amount=source.paid_amount,
                account=source.paid_to,
                supplier=source.party,
                mode_of_payment=source.mode_of_payment,
            ),
        )

    doclist = get_mapped_doc(
        "Payment Entry",
        source_name,
        {
            "Payment Entry": {
                "doctype": "Payment Order",
                "validation": {"docstatus": ["=", 1]},
            }
        },
        target_doc,
        set_missing_values,
    )

# Call the API data processing function
# api_data_endpoint("Sample Data")

