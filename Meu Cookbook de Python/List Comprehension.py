# FORMA 01
lista=[]
for i in range(10):
    lista.append(str(i))
print('Lista 01:', lista)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# FORMA 02
print('Lista 02: ', [str(i) for i in range(10)])
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# FORMA 03
lista03 = [str(i) for i in range(10)]
print('Lista 03: ', lista03)