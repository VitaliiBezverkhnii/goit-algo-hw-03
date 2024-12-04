import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number by ensuring it follows a specific format:
    - Removes all non-numeric characters except for the plus sign ('+').
    - Adds the international country code '+38' if not already present.
    - Ensures the phone number has a valid international code ('+38')

    Parameters:
    phone_number (str): The phone number to be normalized.

    Returns:
    str: The normalized phone number with the international country code '+38' if necessary.
    If the phone number already starts with '+380' or '+38', it is returned unchanged.
    """
    if not isinstance(phone_number, str):
        print("Phone number is not string")
        return ""
    phone_number = re.sub(r"[^+0-9]", "", phone_number)
    if phone_number.startswith('+'):
        if phone_number[1:].startswith('380'):
            return phone_number
        elif not phone_number[1:].startswith('38'):
            return '+38' + phone_number[1:]
    
    if phone_number.startswith('380'):
        return '+' + phone_number
    return '+38' + phone_number

print(normalize_phone("+38/098/810/87/87"))