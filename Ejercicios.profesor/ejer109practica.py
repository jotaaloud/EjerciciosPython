lista=[]

for x in range(10):
    num=int(input("introduce un numero a la lista "))
    lista.append(num)


posicion=0

while posicion<len(lista):
    if lista[x]==5:
        lista.pop(x)
    else:
        posicion=posicion+1

print(lista)
