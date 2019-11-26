"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False


"""

def validate_pin(pin):
    for i in pin:
        if not i.isdigit():
            return False
    try:
        if float(pin) < 0.0:
            return False
    except ValueError:
            return False
    if len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False
