def isPhoneNumberUSA(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


def isPhoneNumberBRA(text):
    if len(text) != 13:
        return False
    for i in range(0, 2):
        if not text[i].isdecimal():
            return False
    if text[2] != '-':
        return False
    for i in range(3, 8):
        if not text[i].isdecimal():
            return False
    if text[8] != '-':
        return False
    for i in range(9, 12):
        if not text[i].isdecimal():
            return False
    return True


if __name__ == '__main__':
    '''phoneNumberUSA = '415-555-4242'
    moshi = 'Moshi moshi'
    print(f"{phoneNumber} is a Phone Number:")
    print(isPhoneNumberUSA(phoneNumber))
    print(f"{moshi} is a phone number:")
    print(isPhoneNumberUSA(moshi))'''

    message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumberUSA(chunk):
            print(f"Phone number found: {chunk}")

    phoneNumberBRA = '16-99999-8888'
    print(f"{phoneNumberBRA} é um número de telefone:")
    print(isPhoneNumberBRA(phoneNumberBRA))
