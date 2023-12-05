# To check  the type of every element in a list by using lambda function 
data = [10,'hello','hi', 37,'world',999,87,351]

check_type = lambda x : 'Integer' if type(x) == int else  'String'

result = list(map(check_type, data))

print(result)