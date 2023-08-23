import frappe
import json
from functools import reduce
from frappe import ValidationError, _, qb, scrub, throw
from frappe.utils import cint, comma_or, flt, getdate, nowdate
from frappe.utils.data import comma_and, fmt_money
import requests
import prompt from erpnext

def is_valid_credit_card_number(card_number):
    # Remove spaces and non-digit characters
    card_number = ''.join(card_number.split())

    # Check if the card number contains only digits
    if not card_number.isdigit():
        return False

    # Apply Luhn algorithm
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        num = int(digit)
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9
        total += num

    return total % 10 == 0
def get_auth_token(requests):
    consumer_key =consumer_key
    consumer_secret=consumer_secret
    api_url=

def initiate_payment(amount, customer_id, card_number, expiration_month, expiration_year, cvv):
    try:
        # Perform basic validation
        if not card_number or not expiration_month or not expiration_year or not cvv:
            frappe.throw("Please provide all credit card details.")

        # Perform more thorough validation here
        if not is_valid_credit_card_number(card_number):
            frappe.throw("Invalid credit card number.")

        if not is_valid_expiration_date(expiration_month, expiration_year):
            frappe.throw("Invalid expiration date.")

        if not is_valid_cvv(cvv):
            frappe.throw("Invalid CVV.")

        # Continue with payment initiation if all validations pass
        payload = {
            "api_key": api_key,
            "api_secret": api_secret,
            "auth_token":auth_token,
            "amount": amount,
            "customer_id": customer_id,
            # Add other required parameters
        }

        # Make the API request
        response = requests.post(api_url,headers=  json=payload)

        if response.status_code == 200:
            response_data = response.json()
            payment_reference = response_data.get("payment_reference")
            
            # Store payment_reference for future reference
            
            return {"payment_reference": payment_reference}
        else:
            frappe.throw("Payment initiation failed")

    except Exception as e:
        frappe.throw(str(e))
