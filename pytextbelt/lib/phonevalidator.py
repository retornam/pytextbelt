import phonenumbers

def validate(phonenumber, country):
    phone = phonenumbers.parse(phonenumber, country)
    return phonenumbers.is_valid_number(phone)

            