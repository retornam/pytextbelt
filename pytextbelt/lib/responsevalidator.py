def validate(phone_number, jsonresponse):
    if ('message' in jsonresponse) and jsonresponse['success']:
        message = jsonresponse['message']
        if message == 'Sorry, texts to this number are disabled.':
            raise Exception(message)
        if message == 'Communication with SMS gateway failed.':
            raise Exception(message)
        if message == 'Could not validate phone# quota.':
            raise Exception(message)
        if message == 'Could not valide IP quota':
            raise Exception(message)
        if message == 'Exceeded quota  for this phone number':
            raise Exception(message)
        if 'Exceeded quota for this IP address' in message:
            raise Exception(message)
    else: 
        return True