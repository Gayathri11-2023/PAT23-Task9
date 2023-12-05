import re
# functions to validate the given values by using regular expression
def validate_regex(pattern, value):
    
    return bool(re.match(pattern, value))

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]'
    return validate_regex(email_regex, email)

def validate_bangladesh_mobile_number(number):
    bd_mobile_regex = r'^\+8801[3-9]\d{8}$'
    return validate_regex(bd_mobile_regex, number)

def validate_usa_telephone_number(number):
    usa_tel_regex = r'^\+1-\d{3}-\d{3}-\d{4}$'
    return validate_regex(usa_tel_regex, number)

def validate_password(password):
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return validate_regex(password_regex, password)

email_address = 'gayu@example.com'
print(f"Is '{email_address}' a valid email address? {validate_email(email_address)}")

mobile_number_bd = '+8801712345678'
print(f"Is '{mobile_number_bd}' a valid mobile number in Bangladesh? {validate_bangladesh_mobile_number(mobile_number_bd)}")

telephone_number_usa = '+1-123-456-7890'
print(f"Is '{telephone_number_usa}' a valid telephone number in the USA? {validate_usa_telephone_number(telephone_number_usa)}")

password = 'Abcd1234!@Efgh5678'
print(f"Is '{password}' a valid 16-character alphanumeric password? {validate_password(password)}")
