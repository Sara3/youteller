import base64
import os
import datetime as dt
import json
import time
import logging
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Import classes
import sys
sys.path.append("classes")
import Plaid_Client
import Firefly_Client

# Load environment variables
load_dotenv()

################
# Initialize app
app = Flask(__name__)

# Create a logger object
logger = logging.getLogger(__name__)
# Set the logging level
logger.setLevel(logging.INFO)
# Add a handler to the logger object
handler = logging.StreamHandler()
logger.addHandler(handler)

# Simple account configuration - only your working Plaid account
accounts = []

# Only add the working bank account
access_token = os.getenv('PLAID_BANK_1_ACCESS_TOKEN')
if access_token and not access_token.startswith('access-development-your'):
    account = {
        'type': 'bank',
        'access_token': os.getenv('PLAID_BANK_1_ACCESS_TOKEN'),
        'pl_id': os.getenv('PLAID_BANK_1_ID'),
        'ff_id': os.getenv('FF_BANK_1_ID'),
        'ff_name': os.getenv('FF_BANK_1_NAME'),
        'cursor': ''
    }
    accounts.append(account)

# Initiate Plaid Controller
plaid = Plaid_Client.Plaid_Client(accounts)

# Initiate Firefly Controller
firefly = Firefly_Client.Firefly_Client(accounts)

# Endpoint used by Firefly III to sync transactions
@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    for account in accounts:
        # Only sync accounts with Plaid IDs
        if account['pl_id'] is not None:
            plaid.transaction_sync(account, firefly)

    return "200"

# Calculate Interest Function
#
# Put code here

if __name__ == '__main__':
    app.run(port=int(os.getenv('PORT', 8000)))