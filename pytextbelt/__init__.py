from lib import phonevalidator
from lib import responsevalidator
from lib import textutils

import requests
import json


def text(phonenumber, message, country='US'):
    if phonevalidator.validate(phonenumber, country):
        uri = textutils.uri_for(country)
        data = {
            'number' : phonenumber,
            'message' : message 
        }
        response = requests.post(uri,data=data)
        body = json.loads(response.text)
        print body
        return responsevalidator.validate(phonenumber, body)
    else:
        raise Exception('Phone number is invalid')