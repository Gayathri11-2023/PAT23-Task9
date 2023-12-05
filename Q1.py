#Expected output for below given code is [10,501,22, 37,100,999,87,351]

data = [10,501,22, 37,100,999,87,351]
result = filter(lambda x : x>4, data)
print(list(result))